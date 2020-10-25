import os

from colorama import Fore


def found(file, line, no, vuln_part, vuln):
    file = os.path.abspath(file)
    print(f'{Fore.GREEN}FOUND:{Fore.RESET} potential {Fore.MAGENTA}{vuln}{Fore.RESET} found!')
    print(f'       Code snippet : {Fore.LIGHTBLACK_EX}{line.replace(vuln_part, Fore.LIGHTRED_EX+vuln_part+Fore.LIGHTBLACK_EX)}{Fore.RESET}')
    print(f'       Position     : line {Fore.YELLOW}{no} {Fore.RESET}in file "{Fore.LIGHTYELLOW_EX}{file.replace(os.path.basename(file), Fore.LIGHTBLUE_EX+os.path.basename(file))}{Fore.RESET}"')
    print()


def error(text, should_exit=True):
    print(f'{Fore.RED}ERROR:{Fore.RESET} {text}{Fore.RESET}.')
    if should_exit:
        exit(-1)


def info(text):
    print(f'{Fore.BLUE}INFO:{Fore.RESET} {text}{Fore.RESET}.')
