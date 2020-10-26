from lib.common.abc import Vulnerability


class LocalFileInclusion(Vulnerability):

    name = 'LOCAL FILE INCLUSION'
    keyname = 'lfi'

    def __init__(self, file_path):
        self.file_path = file_path

    def find(self):
        return self._find(r'(include|require|require_once)\(.*[\$].+\)')
