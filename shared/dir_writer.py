class WriteException(Exception):
    def __init__(self, e: Exception | None) -> None:
        super().__init__(f"error writing dir: {str(e)}")
