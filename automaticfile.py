import os
import shutil

from_dir = "c:/Users/alimu/Downloads"
to_dir = "c:/Users/alimu/OneDrive/Desktop/DownloadImages"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    print("File Name:", name)
    print("File Extension:", extension)
    # Use shutil.move() to move the file from the source path to the destination path
    source_path = os.path.join(from_dir, file_name)
    destination_path = os.path.join(to_dir, file_name)
    shutil.move(source_path, destination_path)
    print(f"Moved '{file_name}' to '{to_dir}'")

print("All files moved successfully!")