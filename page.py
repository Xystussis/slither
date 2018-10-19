class Page:

    def __init__(self):
        self._links = []
        self._meta = []
        self._html = ""
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
