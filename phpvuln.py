import os
import sys
import argparse

from colorama import Fore

from lib.core.banner import BANNER
from lib.core import utils
from lib.core import log

# globals
found = 0


def main():
    vuln_classes = utils.get_vulnerability_classes()

    print(BANNER)

    parser = argparse.ArgumentParser(usage='%(prog)s [options]')

    parser.error = log.error

    parser.add_argument('-p', '--path', help='path', dest='path', metavar='')
    parser.add_argument('-v', '--vulns', help='vulnerabilities to look for', dest='vulns', metavar='', default=','.join(_class.keyname for _class in vuln_classes))

    args = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()
        exit()

    if not os.path.exists(args.path) or not os.path.isdir(args.path):
        log.error('directory not found.')

    if not args.vulns:
        log.error('no vulnerabilities to check is selected.')

    chosen_vulns = args.vulns.lower().split(',')

    for vuln in chosen_vulns:
        if not [_class for _class in vuln_classes if _class.keyname == vuln]:
            log.error(f'unrecognized vulnerability: {vuln}')
            exit()

    global found

    for root, _, directory in os.walk(args.path):
        for file in directory:
            if not file.endswith('.php') and not file.endswith('.html'):
                continue

            file_path = os.path.join(root, file)

            for vuln in chosen_vulns:
                Vulnerability = [_class for _class in vuln_classes if _class.keyname == vuln][0]

                vuln_obj = Vulnerability(file_path)

                for line, no, vuln_part in vuln_obj.find():
                    log.found(file_path, line, no, vuln_part, vuln_obj.name)
                    found += 1

    if found > 0:
        log.info(f'phpvuln finished with {Fore.GREEN}{found} {Fore.RESET}potential vulnerabilit{"y" if found == 1 else "ies"} found.')
    else:
        log.info(f'phpvuln finished, but no potential vulnerabilities were found.')


if __name__ == '__main__':
    main()
