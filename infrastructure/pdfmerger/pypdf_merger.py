import PyPDF2


class PyPDFMerger:
    _merger: PyPDF2.PdfMerger

    def __init__(self) -> None:
        self._merger = PyPDF2.PdfMerger()

    def append(self, path: str):
        try:
            self._merger.append(path)
        except Exception as e:
            Exception(f"PyPDFMerger append: {str(e)}")

    def write(self, path: str):
        try:
            self._merger.write(path)
        except Exception as e:
            Exception(f"PyPDFMerger write: {str(e)}")

    def reset(self):
        self._merger = PyPDF2.PdfMerger()
