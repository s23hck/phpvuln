import re

from typing import List, Tuple
from abc import ABC, abstractmethod


class Vulnerability(ABC):

    def __init__(self, file_path: str):
        self.file_path = file_path
        raise NotImplementedError('you cannot initialise this class')

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def keyname(self) -> str:
        pass

    @abstractmethod
    def find(self) -> List[Tuple[str, int, object]]:
        pass

    def get_lines(self) -> List[List[str]]:
        with open(self.file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = [line.strip() for line in f.readlines()]
        return lines

    def __remove_indent(self, line: str) -> str:
        while line[0] == ' ' or line[0] == '\t':
            line = line[1:]
        return line

    def _find(self, regex: str, ignore_case: bool = True) -> List[Tuple[str, int, object]]:
        vulnerable = []

        for i, line in enumerate(self.get_lines()):

            if ignore_case:
                line.lower()

            match = re.search(f'({regex})', line)

            if match:
                vulnerable.append((self.__remove_indent(line), i, match.group(1)))

        return vulnerable
