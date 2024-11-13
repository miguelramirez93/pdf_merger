import PyPDF2
import os
import re

merger = PyPDF2.PdfMerger()

mergers_indx = {}


def merge_pdf_files_recursive(path="."):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            merge_pdf_files_recursive(full_path)
        else:
            if full_path.endswith(".pdf"):
                add_file_to_merge_indx(path, full_path)


def merge_pdf_files_samename_recursive(path="."):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            merge_pdf_files_samename_recursive(full_path)
        else:
            if full_path.endswith(".pdf"):
                index = get_file_index(full_path)
                add_file_to_merge_indx(index, full_path)


def add_file_to_merge_indx(index, full_path):
    if mergers_indx.get(index) is None:
        mergers_indx[index] = PyPDF2.PdfMerger()
    try:
        mergers_indx[index].append(full_path)
    except Exception as e:
        print(f"file path: {full_path} error:{str(e)}")


def get_file_name_from_path(path="combined") -> str:
    splitted = path.split("/")
    return splitted[-1]


def get_file_index(path="combined") -> str:
    splitted = path.split("/")
    rawFileName = splitted[-1]
    return re.sub(r"\([0-9]+\).pdf", "", rawFileName).replace(".pdf", "")


directory_path = "./target"
outdir_path = "./out"
try:
    merge_pdf_files_recursive(directory_path)
    # merge_pdf_files_samename_recursive(directory_path)
    for dir in mergers_indx:
        mergers_indx[dir].write(f"{outdir_path}/{get_file_name_from_path(dir)}.pdf")
except Exception as e:
    print("Error merging files: " + str(e))
