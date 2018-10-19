from robots import Robots
from page import Page
from bs4 import BeautifulSoup
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
                page.add_link(link)
        # print(soup("a").__getattr__('href'))
        self.add_page(page)
        return page

    def add_page(self, page):
        self._pages.append(page)

    def remove_page(self, page):
        self._pages.remove(page)

    def get_pages(self):
        return self._pages
