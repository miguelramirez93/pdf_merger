import os
import re
from typing import Dict, List

from merger.contracts import Client, DirWriter, FileSearcher


class Merger:
    _client: Client
    _file_searcher: FileSearcher
    _dir_writer: DirWriter

    def __init__(self, client: Client, file_searcher: FileSearcher, dir_writer: DirWriter) -> None:
        self._client = client
        self._file_searcher = file_searcher
        self._dir_writer = dir_writer

    def merge_dir_tree_files(self, in_path: str, out_path_root: str):
        found_files_index = self._file_searcher.search_files(in_path, "pdf")
        for target_path in found_files_index:
            try:
                out_path = os.path.join(
                    *os.path.split(target_path)[1:]).replace(".", "")

                self._dir_writer.write(os.path.join(out_path_root, out_path))

                merge_index: Dict[str, List[str]] = {}
                # walk through found files in current path
                for target_file_path in found_files_index[target_path]:
                    file_index = self._get_file_index(target_file_path)

                    if merge_index.get(file_index) is None:
                        merge_index[file_index] = []

                    merge_index[file_index].append(target_file_path)

                for index in merge_index:
                    self._client.reset()
                    for file_path in merge_index[index]:
                        self._client.append(file_path)
                    target_file_name = f"{index}.pdf"
                    self._client.write(os.path.join(
                        out_path_root, out_path, target_file_name))

            except Exception as e:
                raise Exception(f"merge dir tree files: str{e}")

    def _get_file_index(self, path: str) -> str:
        splitted = os.path.split(path)
        rawFileName = splitted[-1]
        return re.sub(r"-([0-9]).pdf", "", rawFileName).replace(".pdf", "")
