# 🗂️ File Organizer Automation (Python)

This project automatically organizes files from your **Downloads folder** into categorized subfolders (like Images, Documents, Music, Videos, etc.) inside a target folder on your **Desktop**.

---

## 🚀 Features
- Scans your Downloads folder for all files.
- Moves files into categories based on their extension:
  - **Images** → `.jpg`, `.png`, `.gif`, etc.
  - **Documents** → `.pdf`, `.docx`, `.txt`, etc.
  - **Music** → `.mp3`, `.wav`, etc.
  - **Videos** → `.mp4`, `.mov`, etc.
  - **Others** → anything else.
- Creates subfolders automatically if they don’t exist.
- Saves your time by keeping everything clean and organized. ✅

---

## 🛠️ Requirements
- Python 3.x installed on your system.
- Built-in libraries used:
  - `os`
  - `shutil`  
(⚡ No extra installation needed.)

---

## 📂 Setup
1. Clone this repo or copy the code into a file named **file_organizer.py**.
2. Update these two variables in the script:
   ```python
   source_path = r"D:\Downloads"       # Your Downloads folder path
   target_root = r"C:\Users\YourName\Desktop\organized files"   # Target folder on Desktop
## run
python file_organizer.py
