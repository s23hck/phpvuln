import os

from colorama import Fore
from colorama import init

if os.name == 'nt':
    init(convert=True)

BANNER = fr'''{Fore.LIGHTBLUE_EX}       _                  _
  _ __| |_  _ ____ ___  _| |_ _  
 | '_ \ ' \| '_ \ V / || | | ' \ 
 | .__/_||_| .__/\_/ \_,_|_|_||_| {Fore.RESET}v0.1.0{Fore.LIGHTBLUE_EX}
 |_|       |_|
 {Fore.RESET}by checksum (@computergoon)
'''