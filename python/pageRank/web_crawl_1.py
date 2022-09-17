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

starturl = input('Enter web url or enter: ')
if ( len(starturl) < 1 ) : starturl = 'http://www.dr-chuck.com/'
if ( starturl.endswith('/') ) : starturl = starturl[:-1]
web = starturl
if ( starturl.endswith('.htm') or starturl.endswith('.html') ) :
    pos = starturl.rfind('/')
    web = starturl[:pos]

#print(pos, web)

document = urlopen(web, context=ctx)
html = document.read()
print(type(html))
print(type(document), document.getcode(), document.info().get_content_type())
soup = BeautifulSoup(html, "html.parser")
print(type(soup))
#print(soup)
tags = soup('a')
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
