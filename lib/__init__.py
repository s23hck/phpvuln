import os

from colorama import Fore
from colorama import init

if os.name == 'nt':
    init(convert=True)