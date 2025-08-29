import os
import shutil

# Define extension → folder mapping
EXTENSIONS_MAP = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".mp3": "Music",
    ".wav": "Music",
    ".zip": "Archives",
    ".rar": "Archives",
    ".exe": "Programs"
}

# Source folder (the messy folder with files you want to organize)
source_path = "Source folder"   # change to your actual folder

# Target folder (where organized subfolders will be created)
target_root = "Target folder"  # change to your desired target folder


def organize_files():
    # Loop through all items in source folder
    for filename in os.listdir(source_path):
        file_path = os.path.join(source_path, filename)

        # Skip if it's a folder
        if os.path.isdir(file_path):
            continue

        # Get file extension (lowercase for safety)
        _ , ext = os.path.splitext(filename)
        ext = ext.lower()

        # Find destination folder
        folder_name = EXTENSIONS_MAP.get(ext, "Others")
        dest_folder = os.path.join(target_root, folder_name)

        # Create folder if not exists
        os.makedirs(dest_folder, exist_ok=True)

        # Move the file
        shutil.move(file_path, os.path.join(dest_folder, filename))
        print(f"Moved: {filename} → {folder_name}")


# Run the organizer
if __name__ == "__main__":
    organize_files()
    print("\n✅ All files have been organized successfully!")
