import re

from lib.common.abc import Vulnerability


class XSS(Vulnerability):

    name = 'CROSS-SITE SCRIPTING (XSS)'
    keyname = 'xss'

    def __init__(self, file_path):
        self.file_path = file_path

    def find(self):
        return []

    def is_user_input(self, field):
        for line in self.get_lines():
            match = re.search(r'_(GET|POST|DELETE|PUT|PATCH|OPTIONS)\[(.*)%s.*\]' % field, line)

            if match:
                return True

        return False
