from lib.common.abc import Vulnerability


class SQLInjection(Vulnerability):

    name = 'SQL INJECTION'
    keyname = 'sqli'

    def __init__(self, file_path):
        self.file_path = file_path

    def find(self):
        return self._find(r'(mysqli?_|\->)query\(("|\').*[\$].+("|\')\)', False)
