"""
web crawler 2

In this version, we will add database into the code,
so that the retrieve the webpage will be stored in the database
and the retrieving process can be restart and continued.

Data structure of the database:
1. table pages to store all the pages retrieved.
- id, url, html, error, old_rank, new_rank
the rank fields are prepared for the later ranking
html: is the content of the page which should be html format
error: when connect to the server, it can be disrupted with different reasons
use error field to track the error number.
2. table links to store the pair of links.
- from_id is the id of the original page and to_id is the id of the pointed page
3. table webs to store the start page


author: Yerong Chen
date: 2022-09-18
"""

import urllib.error
import ssl
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sqlite3

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# establish the database and get the cursor (similar as file handle)
conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

# create tables
cur.execute('''CREATE TABLE IF NOT EXISTS Pages
    (id INTEGER PRIMARY KEY, url TEXT UNIQUE, html TEXT,
     error INTEGER, old_rank REAL, new_rank REAL)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Links
    (from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))''')

cur.execute('''CREATE TABLE IF NOT EXISTS Webs (url TEXT UNIQUE)''')

# Check to see if we are already in progress...
cur.execute('''SELECT id,url FROM Pages WHERE html is NULL
and error is NULL ORDER BY RANDOM() LIMIT 1''')
row = cur.fetchone()
if row is not None:
    print("Restarting existing crawl.  Remove spider.sqlite to start a fresh crawl.")
else :
#prepare the URL for the retrieving
    starturl = input('Enter web url or enter: ')
    if ( len(starturl) < 1 ) : starturl = 'http://www.dr-chuck.com/'
    if ( starturl.endswith('/') ) : starturl = starturl[:-1]
    web = starturl
    if ( starturl.endswith('.htm') or starturl.endswith('.html') ) :
        pos = starturl.rfind('/')
        web = starturl[:pos]
    # insert the start page into table Webs and table Pages
    # Since this is a fresh start, the Webs and Pages table shall be empty
    if ( len(web) > 1 ) :
        cur.execute('INSERT OR IGNORE INTO Webs (url) VALUES ( ? )', ( web, ) )
        cur.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', ( starturl, ) )
        conn.commit()

# Get the start page and print it
# it seems that in the Webs table there is only one start page
cur.execute('''SELECT url FROM Webs''')
webs = list()
for row in cur:
    webs.append(str(row[0]))

print(webs)


many = 0
while True:
    # work on the exit condition
    if ( many < 1 ) :
        sval = input('How many pages you want to retrieve:')
        # without giving a number, the program will be terminated
        if ( len(sval) < 1 ) : break
        many = int(sval)
    many = many - 1

    # if the program starts fresh, there should be only one page in the Pages table
    # than this statement will return this page
    # if the program is resumed (with many pages in the table)
    # this statement will pick up one unretrieved page randomly
    cur.execute('''SELECT id,url FROM Pages WHERE html is NULL
    and error is NULL ORDER BY RANDOM() LIMIT 1''')

    try:
        row = cur.fetchone()
        fromid = row[0]
        url = row[1]
    except:
        print('No unretrieved HTML pages found')
        many = 0
        break

    print(fromid, url, end=' ')
    # If we are retrieving this page, there should be no links from it
    # this statement is just make it safe
    cur.execute('DELETE from Links WHERE from_id=?', (fromid, ) )

    # open the url
    # document is like a file handel, and includes all the header of the page
    try:
        document = urlopen(web, context=ctx)

        html = document.read()
        #print(type(html))
        #print(type(document), document.getcode(), document.info().get_content_type())
        # in this case, the program is able to open the link
        # and get response from the server, but the header of the response indicates
        # that the page has error, therefore we won't retrieve the page but set the
        # error in the table
        if document.getcode() != 200:
            print('Error on page: ', document.getcode())
            cur.execute('UPDATE Pages SET error=? WHERE url=?', (document.getcode(), url) )

        if document.info().get_content_type() != 'text/html':
            print('Non-html page!', document.info().get_content_type())
            cur.execute('DELETE FROM Pages WHERE url=?', ( url, ) )
            conn.commit()
            continue

        # print the length of the content
        print('('+str(len(html))+')', end=' ')

        # use Beautifulsoup can parse the input byte data into html
        # it also removes the errors from html
        soup = BeautifulSoup(html, "html.parser")
        #print(type(soup))

    # use ctrl+c to terminate the program
    except KeyboardInterrupt:
        print('')
        print('Program interrupted by user...')
        break
    except:
        print("Unable to retrieve or parse page")
        cur.execute('UPDATE Pages SET error=-1 WHERE url=?', (url, ) )
        conn.commit()
        continue

    # till here we retrieve one page successfully and we add the html content
    # into the table
    cur.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', ( url, ) )
    cur.execute('UPDATE Pages SET html=? WHERE url=?', (memoryview(html), url ) )
    conn.commit()

    # use soup('a') can retrieve all the html with <a href=...>...<\a>
    # and save it in a list
    tags = soup('a')
    #print(tags)
    count = 0
    #c = 1
    for tag in tags:
        href = tag.get('href', None)
        # No href in this page, than we begin to crawl next page
        if ( href is None ) : continue

        up = urlparse(href)
        if ( len(up.scheme) < 1 ) :
            href = urljoin(web, href)
        ipos = href.find('#')
        if ( ipos > 1 ) : href = href[:ipos]
        if ( href.endswith('.png') or href.endswith('.jpg') or href.endswith('.gif') ) : continue
        if ( href.endswith('/') ) : href = href[:-1]
        if ( len(href) < 1 ) : continue
        #print('***'+str(c)+'***    ',href)
        #print(up)
        #c += 1

        # As the webs hosts the start page
        # This means we will ignore all the links pointing outside
        # only subpages will be add to the table
        found = False
        for web in webs:
            if ( href.startswith(web) ) :
                found = True
                break
        if not found :
            #print('Outside pages will be ignored.')
            continue

        cur.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) \
            VALUES ( ?, NULL, 1.0 )', ( href, ) )
        count = count + 1
        conn.commit()

        cur.execute('SELECT id FROM Pages WHERE url=? LIMIT 1', ( href, ))
        try:
            row = cur.fetchone()
            toid = row[0]
        except:
            print('Could not retrieve id')
            continue
        # print fromid, toid
        cur.execute('INSERT OR IGNORE INTO Links (from_id, to_id) \
            VALUES ( ?, ? )', ( fromid, toid ) )


    print(count)

cur.close()
