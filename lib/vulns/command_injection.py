from lib.common.vuln.abc import Vulnerability


class CommandInjection(Vulnerability):

    name = 'COMMAND INJECTION'
    keyname = 'cmdi'

    def __init__(self, file_path):
        self.file_path = file_path

    def find(self):
        return self._find(r'\s+(exec|system|shell_exec)\(.*[\$].+\)', False)
