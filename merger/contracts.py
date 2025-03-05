from abc import ABCMeta, abstractmethod
from typing import Dict, List


class Client(metaclass=ABCMeta):
    @abstractmethod
    def append(self, path: str):
        pass

    @abstractmethod
    def write(self, path: str):
        pass

    @abstractmethod
    def reset(self):
        pass


class FileSearcher(metaclass=ABCMeta):
    @abstractmethod
    def search_files(self, path: str, ext: str) -> Dict[str, List[str]]:
        pass


class DirWriter(metaclass=ABCMeta):
    @abstractmethod
    def write(self, dir_path: str):
        pass
