# Challenge: Move All Image Files to a New Directory
# from RealPython, Python Basics, chapter 12.4
#

from pathlib import Path

# data_path =Path.home() / "practice_files"
data_path = Path.cwd() / "practice_files"
# print(data_path)
if data_path.exists():
    new_images_dir = data_path / "images"
    new_images_dir.mkdir(exist_ok = True)
    for files in data_path.rglob("*.*"):
       if files.suffix == ".png" or files.suffix == ".jpg" or files.suffix == ".gif":
          files.replace(new_images_dir / files.name)
