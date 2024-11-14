import PyPDF2
from abc import ABC, abstractmethod


class Merger(ABC):
    _mergers_indx = {}

    @abstractmethod
    def merge_pdf(self, path: str):
        pass

    def add_file_to_merge_indx(self, index, full_path):
        if self._mergers_indx.get(index) is None:
            self._mergers_indx[index] = PyPDF2.PdfMerger()
        try:
            self._mergers_indx[index].append(full_path)
        except Exception as e:
            print(f"file path: {full_path} error:{str(e)}")

    def write_merged_files(self, outdir_path: str):
        try:
            for indx in self._mergers_indx:
                self._mergers_indx[indx].write(f"{outdir_path}/{indx}.pdf")
        except Exception as e:
            print("Error merging files: " + str(e))
