from abc import ABCMeta, abstractmethod
from typing import List


class FolderReader(metaclass=ABCMeta):
    @abstractmethod
    def list_elements(self, path: str) -> List[str]:
        pass

    @abstractmethod
    def is_dir(self, path: str) -> bool:
        pass
