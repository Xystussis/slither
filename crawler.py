import concurrent.futures
import urllib.request


class Crawler:

    def __init__(self, urls, max_threads=5):
        self._urls = urls
        self._results = []
        self._max_threads = max_threads

    @staticmethod
    def load_url(url, timeout):
        with urllib.request.urlopen(url, timeout=timeout) as conn:
            return conn.read()

    def begin_crawl(self):
        # Start the load operations and mark each future with its URL
        with concurrent.futures.ThreadPoolExecutor(max_workers=self._max_threads) as executor:
            future_to_url = {executor.submit(self.load_url, url, 60): url for url in self._urls}
            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    data = future.result()
                except Exception as exc:
                    print('%r generated an exception: %s' % (url, exc))
                else:
                    self._results.append({"data": data, "url": url})
                    print('%r page is %d bytes' % (url, len(data)))
        return self._results
