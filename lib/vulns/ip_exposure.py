import ipaddress

from lib.common.abc import Vulnerability


class IPExposure(Vulnerability):

    name = 'IP EXPOSURE'
    keyname = 'ips'

    def __init__(self, file_path):
        self.file_path = file_path

    def find(self):
        return [(code, line_no, match) for code, line_no, match in self._find(r'[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}') if not ipaddress.IPv4Interface(match).is_private]
