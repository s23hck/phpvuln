import re

from lib.common.abc import Vulnerability


class Credentials(Vulnerability):

    name = 'CONFIGURATION CREDENTIALS'
    keyname = 'creds'

    def __init__(self, file_path):
        self.file_path = file_path

    def find(self):
        vulns = []
        for code, line_no, match in self._find(r'\$[^\->\$]*(pwd|pass|key|secret|token)[\w]*\s*=\s*("|\').*("|\')'):
            password = re.search(r'("|\')(.*)("|\')', match)
            if not password:
                continue
            if len(password.group(2)) == 0:
                continue
            vulns.append((code, line_no, match))
        return vulns

    def _is_hashed(self, x):
        return bool(re.match(r'^([a-fA-F0-9\$\.]{32}|[a-fA-F0-9\$\.]{64})$', x))
