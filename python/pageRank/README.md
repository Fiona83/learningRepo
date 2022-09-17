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

```
if ( starturl.endswith('/') ) : starturl = starturl[:-1]
```

