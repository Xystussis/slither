from bs4 import BeautifulSoup


class Page:

    def __init__(self, url="", site=""):
        self._links = []
        self._meta = []
        self._html = ""
        self._url = url
        self._site = site
        self._request = None

    def get_html(self):
        return self._html

    def get_links(self):
        return self._links

    def get_meta(self):
        return self._meta

    def set_html(self, html):
        self._html = html

    def add_link(self, link):
        self._links.append(link)

    def remove_link(self, link):
        self._links.remove(link)

    def add_meta(self, meta):
        self._meta.append(meta)

    def remove_meta(self, meta):
        self._meta.remove(meta)

    def set_request(self, request):
        self._request = request

    def get_request(self):
        return self._request

    def set_url(self, url):
        self._url = url

    def get_url(self):
        return self._url

    def parse_page(self, robot):
        soup = BeautifulSoup(self.get_html(), 'html.parser')

        for link in (item['href'] for item in soup.find_all('a', href=True) if
                     item['href'] and item['href'] != "#" and item['href'] != '/'):
            if robot.can_view(link) and link not in self.get_links():
                if link[0] == "/":
                    link = f"{self._site}{link}"
                self.add_link(link)
