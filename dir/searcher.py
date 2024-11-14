import os
from typing import Dict, List

from dir.contracts import FolderReader


class Searcher:
    _folder_reader: FolderReader

    def __init__(self, reader: FolderReader) -> None:
        self._folder_reader = reader

    def search_files(self, path: str, ext: str) -> Dict[str, List[str]]:
        search_res: Dict[str, List[str]] = {}
        self._search_files_recursive(path, ext, search_res)
        return search_res

    def _search_files_recursive(self, path: str, ext: str, files_index: Dict[str, List[str]] = {}):
        try:
            for elemnt_relative_path in self._folder_reader.list_elements(path):

                elemnt_path: str = os.path.join(path, elemnt_relative_path)

                if self._folder_reader.is_dir(elemnt_path):
                    self._search_files_recursive(elemnt_path, ext, files_index)
                elif elemnt_path.endswith(f".{ext}"):
                    if files_index.get(path) is None:
                        files_index[path] = []
                    files_index[path].append(elemnt_path)
        except Exception as e:
            raise Exception(f"search files recursive: {str(e)}")
