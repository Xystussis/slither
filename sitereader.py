from robots import Robots
from page import Page
from bs4 import BeautifulSoup
from crawler import Crawler
import requests


class SiteReader:
    def __init__(self, site):
        self._site = site
        self._pages = []
        self._robot = Robots(site)

    def read(self):
        if not self._robot.can_view('/'):
            raise ConnectionError("You are not allowed to scrape this site.")
        page = Page()
        request = requests.get(self._site)
        page.set_request(request)
        page.set_html(request.text)

        soup = BeautifulSoup(page.get_html(), 'html.parser')

        for link in (item['href'] for item in soup.find_all('a', href=True) if
                     item['href'] and item['href'] != "#" and item['href'] != '/'):
            if self._robot.can_view(link) and link not in page.get_links():
                if link[0] == "/":
                    link = f"{self._site}{link}"
                page.add_link(link)
        self.add_page(page)
        return page

    # This is a TEST method - it is ONLY designed to crawl the first page of the main sites linked pages.
    def crawl(self):
        if len(self._pages) > 0:
            crawler = Crawler(self._pages[0].get_links())
            for result in crawler.begin_crawl():
                page = Page(site=self._site)
                page.set_url(result["url"])
                page.set_html(result["data"])
                page.parse_page(self._robot)
                print(f'{page.get_url()} has {len(page.get_links())} links')
                self.add_page(page)
        # print(self._pages)

    def add_page(self, page):
        self._pages.append(page)

    def remove_page(self, page):
        self._pages.remove(page)

    def get_pages(self):
        return self._pages
