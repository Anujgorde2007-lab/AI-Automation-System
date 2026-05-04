"""
AI-inspired file automation system for organizing real-world data efficiently.
"""
import os
import shutil

# Folder path (change to your folder)
source_folder = "test_folder"

# File type categories
file_types = {
    "Images": [".jpg", ".png"],
    "Documents": [".pdf", ".txt"],
    "Videos": [".mp4"],
}

def organize_files():
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        if os.path.isfile(file_path):
            for folder, extensions in file_types.items():
                if filename.lower().endswith(tuple(extensions)):
                    target_folder = os.path.join(source_folder, folder)

                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)

                    shutil.move(file_path, os.path.join(target_folder, filename))
                    print(f"Moved: {filename} → {folder}")

if _name_ == "_main_":
    organize_files()
