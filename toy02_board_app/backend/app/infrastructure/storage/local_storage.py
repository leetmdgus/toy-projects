import os
from fastapi import UploadFile

class LocalStorage:
    def __init__(self, base_path: str = "uploads"):
        self.base_path = base_path
        os.makedirs(base_path, exist_ok=True)

    def save_file(self, file: UploadFile) -> str:
        file_path = os.path.join(self.base_path, file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        return file_path