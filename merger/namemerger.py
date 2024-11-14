from merger.merger import Merger
import os
import re


class NameMerger(Merger):
    def __init__(self) -> None:
        super().__init__()

    def merge_pdf(self, path: str):
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                self.merge_pdf(full_path)
            else:
                if full_path.endswith(".pdf"):
                    index = self.get_file_index(full_path)
                    self.add_file_to_merge_indx(index, full_path)

    def get_file_index(self, path: str) -> str:
        splitted = path.split("/")
        rawFileName = splitted[-1]
        return re.sub(r"\([0-9]+\).pdf", "", rawFileName).replace(".pdf", "").strip()
