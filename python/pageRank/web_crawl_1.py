"""
web crawler basic

author: Yerong Chen
date: 2022-09-17
"""

import urllib.error
import ssl
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#prepare the URL for the retrieving
starturl = input('Enter web url or enter: ')
if ( len(starturl) < 1 ) : starturl = 'http://www.dr-chuck.com/'
if ( starturl.endswith('/') ) : starturl = starturl[:-1]
web = starturl
if ( starturl.endswith('.htm') or starturl.endswith('.html') ) :
    pos = starturl.rfind('/')
    web = starturl[:pos]

# open the url
# document is like a file handel, and includes all the header of the page
try:
    document = urlopen(web, context=ctx)
except Exception as err:
    print('Unable to retrieve the page.', err)
    quit()

html = document.read()
print(type(html))
print(type(document), document.getcode(), document.info().get_content_type())
if document.getcode() != 200:
    print('Error on page: ', document.getcode())
    quit()
if document.info().get_content_type() != 'text/html':
    print('Non-html page!', document.info().get_content_type())
    quit()

# use Beautifulsoup can parse the input byte data into html
# it also removes the errors from html
soup = BeautifulSoup(html, "html.parser")
print(type(soup))
#print(soup)

# use soup('a') can retrieve all the html with <a href=...>...<\a>
# and save it in a list
tags = soup('a')
#print(tags)
count = 1
for tag in tags:
    href = tag.get('href', None)
    up = urlparse(href)
    if ( len(up.scheme) < 1 ) :
        href = urljoin(web, href)
    ipos = href.find('#')
    if ( ipos > 1 ) : href = href[:ipos]
    if ( href.endswith('.png') or href.endswith('.jpg') or href.endswith('.gif') ) : continue
    if ( href.endswith('/') ) : href = href[:-1]
    print('***'+str(count)+'***    ',href)
    #print(up)
    count += 1
