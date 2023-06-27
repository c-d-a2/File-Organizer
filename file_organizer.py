import os
import shutil
import sys
import winreg

def organize_files(directory):
    os.chdir(directory)

    file_extension_directory_mapping = {
        "Audio": [".aac", ".aiff", ".flac", ".mp3", ".m4a", ".ogg", ".wav", ".wma"],
        "Compressed": [".7z", ".bz2", ".gz", ".rar", ".zip"],
        "Document": [
            ".doc",
            ".docx",
            ".html",
            ".pdf",
            ".ppt",
            ".pptx",
            ".txt",
            ".odt",
            ".pdf",
            ".ods",
            ".csv",
            "odp",
        ],
        "Image": [".gif", ".jpeg", ".jpg", ".png", ".svg"],
        "Video": [".avi", ".mov", ".mp4", ".mkv"],
        "Disk": [".iso"],
        "Application": [".exe", ".msi", ".app", ".deb"],
    }

    for filename in os.listdir():
        if os.path.isfile(filename):
            file_extension = os.path.splitext(filename)[1].lower()
            print(f"Filename: {filename}, Extension: {file_extension}")

            target_directory = "Others"
            for category, extensions in file_extension_directory_mapping.items():
                if file_extension in extensions:
                    target_directory = category
                    break

            if not os.path.exists(target_directory):
                os.makedirs(target_directory)

            try:
                shutil.move(filename, target_directory)
            except Exception as e:
                print(f"Error moving file: {filename}. Error: {e}")


def find_python_exe():
    python_exe_path = sys.executable
    if not python_exe_path:
        raise Exception("Cannot find python executable path.")
    return python_exe_path


if __name__ == "__main__":
    organize_files(sys.argv[1])
    script_path = r"C:\\path\\to\\your\\script"
    python_exe_path = find_python_exe()

    command = f'"{python_exe_path}" "{script_path}" "%V"'

    try:
        key_shell = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r"Directory\\Background\\shell\\Sort")
        winreg.SetValue(key_shell, "", winreg.REG_SZ, "Sort Files")
        
        key_command = winreg.CreateKey(key_shell, r"command")
        winreg.SetValue(key_command, "", winreg.REG_SZ, command)
    except Exception as e:
        print("Failed to create registry key:", e)
