import re

from lib.common.abc import Vulnerability


class CommandInjection(Vulnerability):

    name = 'COMMAND INJECTION'
    keyname = 'cmdi'

    def __init__(self, file_path):
        self.file_path = file_path
        super().__init__(file_path)

    def find(self):
        vulns = []
        for code, no, match in self._find(r'(\s+|^)(exec|system|shell_exec)\(.*[\$].+\)', False):
            if re.search(r'(exec|system|shell_exec)\(.*escapeshellarg\(.*[\$].+\).*\)', match):
                continue
            vulns.append((code, no, match))
        return vulns
