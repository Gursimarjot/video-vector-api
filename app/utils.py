
import os
from uuid import uuid4

def ensure_dir_exists(dir_path: str):
    os.makedirs(dir_path, exist_ok=True)

def generate_unique_filename(extension: str = ".jpg") -> str:
    return f"{uuid4()}{extension}"

def save_upload_file(upload_file, destination_path: str):
    with open(destination_path, "wb") as buffer:
        buffer.write(upload_file.file.read())
