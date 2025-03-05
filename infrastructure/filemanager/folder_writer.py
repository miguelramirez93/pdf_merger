import os


class OSFolderWriter:
    def write(self, dir_path: str):
        os.makedirs(dir_path, exist_ok=True)
