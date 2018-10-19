# slither
Python 3 Tools for Crawling Pages

### Purpose
This is a custom tool set for my personal use, with the idea of always honouring the robots.txt / robot meta data for a site.

### Requirements

Please make sure you have BeautifulSoup installed: 
https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup

```
python3 -m pip install bs4
```

### Usage

```
python3 startup.py http://yoursitehere.com
```

### Process

Crawler will check for robots, parse it for the rules,
and react accordingly. In theory it should only crawl links that are not
explicitly disallowed in the robots.txt (for now.)