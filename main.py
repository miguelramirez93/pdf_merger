from merger.foldermerger import FolderMerger

directory_path = "./target"
outdir_path = "./out"
merger = FolderMerger()
try:
    merger.merge_pdf(directory_path)
    merger.write_merged_files(outdir_path)
except Exception as e:
    print("Error merging files: " + str(e))
