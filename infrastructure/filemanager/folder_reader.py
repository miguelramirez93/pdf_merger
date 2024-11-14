import os
from typing import List


class OSFolderReader:
    def list_elements(self, path: str) -> List[str]:
        try:
            return os.listdir(path)
        except Exception as e:
            raise Exception(f"list elements: {str(e)}")

    def is_dir(self, path: str) -> bool:
        try:
            return os.path.isdir(path)
        except Exception as e:
            raise Exception(f"is dir: {str(e)}")
