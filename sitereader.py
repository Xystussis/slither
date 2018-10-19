from robots import Robots
from page import Page

import requests


class SiteReader:
    def __init__(self, site):
        self._site = site
        self._robot = Robots(site)

    def read(self):
        if not self._robot.can_view('/'):
            raise ConnectionError("You are not allowed to scrape this site.")
        page = Page()
        request = requests.get(self._site)
        page.set_request(request)
        page.set_html(request.text)
        return page
