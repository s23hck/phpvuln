from lib.common.vuln.abc import Vulnerability


class Credentials(Vulnerability):

    name = 'CONFIGURATION CREDENTIALS'
    keyname = 'creds'

    def __init__(self, file_path):
        self.file_path = file_path

    def find(self):
        vulnerable = []

        for code, line_no, match in self._find(r'\$[^\->]*(password|pwd|pass)\s+=\s+("|\').*("|\')'):
            #password = re.search(r'.*=.*("|\')(.+?)("|\')', code)
            # if not password:
            #    continue

            # if self._is_hashed(password.group(2)):
            #    continue

            vulnerable.append((code, line_no, match))

        return vulnerable
