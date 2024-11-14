from merger.merger import Merger
import os


class FolderMerger(Merger):
    def __init__(self) -> None:
        super().__init__()

    def merge_pdf(self, path: str):
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                self.merge_pdf(full_path)
            else:
                if full_path.endswith(".pdf"):
                    self.add_file_to_merge_indx(path, full_path)
