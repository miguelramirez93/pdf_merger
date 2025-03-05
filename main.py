from typing import Any

from dir.searcher import Searcher
from infrastructure.filemanager.folder_reader import OSFolderReader
from infrastructure.filemanager.folder_writer import OSFolderWriter
from infrastructure.pdfmerger.pypdf_merger import PyPDFMerger
from merger.merger import Merger

try:
    # init dependencies
    _folder_reader: Any = OSFolderReader()
    _searcher: Any = Searcher(reader=_folder_reader)
    _merger_cli: Any = PyPDFMerger()
    _dir_writer: Any = OSFolderWriter()


# Execution
    _merger = Merger(client=_merger_cli, file_searcher=_searcher,
                     dir_writer=_dir_writer)

    print("Merging process started, please wait...")
    _merger.merge_dir_tree_files("./in", "./out")
except Exception as e:
    print(f"There was an error running the merger: {str(e)}")
finally:
    input("press any key to exit...")
