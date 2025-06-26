from pathlib import Path

import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import easyocr

from step_1 import IN_DIR


def read_text(path: Path) -> list:
    reader = easyocr.Reader(["ko", "en"], verbose=False)
    return reader.readtext(path.read_bytes())


if __name__ == "__main__":
    path = IN_DIR / "ocr.jpg"
    print(read_text(path))