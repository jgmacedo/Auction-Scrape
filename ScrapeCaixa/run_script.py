import subprocess

# List of Python files to run in order
file_paths = [
    "folder_cleaner.py",
    "scraper.py",
    "upload_to_drive.py",
    "folder_cleaner.py"
]

# Run each file in order
for file_path in file_paths:
    subprocess.run(["python3", file_path])
