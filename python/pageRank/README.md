# This is all about "Page Ranking Project"


## 1: Simple web crawler
We start from a website and try to retrieve all the links in it.
Then we choose one or more of the links to redo the retrieving.

We will start the crawler from the website: http://www.dr-chuck.com/
(This website is from the course Python for Everyone and is safe to be crawled.)
code: web_crawl_1.py

### Step 1: prepare the url
#### 1.1 remove the last / from the url
Use endswith() function to check if the url ends with /.
If it is so, use str[:-1] to strip the last /.

```Python
if ( starturl.endswith('/') ) : starturl = starturl[:-1]
```
#### 1.2 By subpage retrieve the server url instead
If the url ends with '.htm' or '.html', we will remove the whole page name and
retrieve the server url instead. For example, if the url is http://www.dr-chuck.com/page1.htm, we will go back to retrieve http://www.dr-chuck.com instead.

```Python
if ( starturl.endswith('.htm') or starturl.endswith('.html') ) :
    pos = starturl.rfind('/')
    web = starturl[:pos]
```

### Step 2: open the url and parse the data
#### 2.1 Open the url and retrieve content
Use urlopen will return a HTTP handle (like a file handle). It contains a lot of information such as the header of the page and also the content of the page. Use read() method can retrieve the data from the handle. The data is in the format of **byte**. If you want to read the data in unicode, you can use ***decode()*** function.

```Python
document = urlopen(web, context=ctx)
html = document.read()
```
Use ***getcode()*** method can check if the retrieve is successful (200 = ok).
Use ***info().get_content_type()*** can check if the text format of the content.

```Python
if document.getcode != 200:
    print('Error on page: ', document.getcode())
    quit()
if document.info().get_content_type() != 'html/text':
    print('Non-html page!', document.info().get_content_type())
    quit()
```


#### 2.2 Parse the html data using BeautifulSoup
Use ***BeautifulSoup(data, "html.parser")*** will return a handle and soup('a') can return a list of all the a tag \<a href="..."\>...\</a\>.

```Python
soup = BeautifulSoup(html, "html.parser")
tags = soup('a')
```

Now with a for loop we can retrieve all the links in the page.

#### 2.3 Retrieve url from the \<a\>\</a\> tag
The following code can retrieve the url from the \<a href="..."\>...\</a\> tag. href will be the http://..... address.

```Python
href = tag.get('href', None)
up = urlparse(href)
```

Interesting thing is use ***urlparse()*** method we can slpit the url into several parts. Please see the example below.
```
https://www.coursera.org/instructor/drchuck
ParseResult(scheme='https', netloc='www.coursera.org', path='/instructor/drchuck', params='',
 query='', fragment='')
```
Use the results of *urlparse()* we can cleanup retrieved url. \# in the URL is to tell the browser, when open the page please scroll down to the position specified by \#. Since this is a pure browser action, and has nothing to do with retrieving data from server, we can remove all the things after \#.

```Python
if ( len(up.scheme) < 1 ) :
      href = urljoin(web, href)
ipos = href.find('#')
if ( ipos > 1 ) : href = href[:ipos]
```
