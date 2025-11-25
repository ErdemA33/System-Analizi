🖥️ System Inspector & Cleaner

A modern desktop application for real-time system monitoring and basic cleanup operations. It provides a clean dark interface and allows users to track system performance easily.

🎯 Overview

System Inspector & Cleaner monitors CPU, RAM, and (if available) GPU usage, keeps timestamped logs, and offers simple cleanup tools for temporary and unnecessary files. It can also be packaged as a standalone executable for easy distribution.

✅ Features

Real-time monitoring (CPU / RAM / GPU)

Timestamped logging

Temporary file cleanup

Dark UI (customtkinter)

Executable build support via PyInstaller

🖼️ Screenshots

(Add your screenshots here)

📂 Project Structure

project
├─ ui
│ └─ main.py
├─ core
│ ├─ monitor.py
│ ├─ cleaner.py
│ └─ logger.py
└─ logs

🚀 How to Run

Install Python 3.10+

Install dependencies:
pip install -r requirements.txt

Start the application:
python main.py

🛠️ Build .EXE

Use PyInstaller:
pyinstaller --noconsole --onefile --add-data "core;core" ui/main.py

The generated .exe file will be located in the dist/ folder.

⚠️ Notes

Cleanup operations target safe directories only.

Some actions may require administrator permissions.

Log files are stored locally on the device.

👤 Developer

Erdem Aydın
