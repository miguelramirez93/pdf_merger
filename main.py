import PyPDF2
import os

merger = PyPDF2.PdfMerger()

mergers_indx = {}


def merge_pdf_files_recursive(path="."):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            merge_pdf_files_recursive(full_path)
        else:
            if full_path.endswith(".pdf"):
                if mergers_indx.get(path) is None:
                    mergers_indx[path] = PyPDF2.PdfMerger()
                try:
                    mergers_indx[path].append(full_path)
                except Exception as e:
                    print(f"file path: {full_path} error:{str(e)}")


def get_file_name_from_path(path="combined") -> str:
    splitted = path.split("/")
    return splitted[-1]


directory_path = "./target"
outdir_path = "./out"
try:
    merge_pdf_files_recursive(directory_path)
    for dir in mergers_indx:
        mergers_indx[dir].write(f"{outdir_path}/{get_file_name_from_path(dir)}.pdf")
except Exception as e:
    print("Error merging files: " + str(e))
