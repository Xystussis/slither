import requests
import re


class Robots:

    def __init__(self, filename):
        self._filename = filename
        self._disallowed = []
        self._fetchFile()
        self._parse()

    def _fetchFile(self):
        self._file_contents = requests.get(self._filename)

    def _parse(self):
        lines = self._file_contents.text.split('\n')
        user_agent = "*"
        for pair in [line.split(':') for line in lines if len(line.split(':')) == 2]:

            instruction = pair[0].lower().strip()
            value = pair[1]
            if instruction == "user-agent":
                user_agent = value.strip()
            if user_agent == "*" or user_agent == "our name?":
                if instruction.lower() == "disallow":
                    self._disallowed.append(value.strip())

    def _found_as_regex(self, pattern_string, search_item):
        pattern_string = pattern_string.replace("*", ".*")
        pattern_string = pattern_string.replace("/", r'\/')
        pattern_string = pattern_string.replace("?", r'\?')
        pattern_string = pattern_string.replace("$", r'.*')
        pattern = re.compile(pattern_string)
        matches = pattern.match(search_item)
        if matches:
            return True
        return False

    def can_view(self, url):
        if url in self._disallowed:
            return False
        for no_access_part in self._disallowed:
            if no_access_part in url or self._found_as_regex(no_access_part, url):
                # print(f"{no_access_part}: {self._found_as_regex(no_access_part, url)}")
                return False
        return True

        # return url not in self._disallowed

    def print_disallowed(self):
        print(self._disallowed)
