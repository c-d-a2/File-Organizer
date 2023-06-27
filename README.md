#File Organizer Script

This script helps you organize your files in any specified directory based on their file types (extensions). Files are moved into directories named after their category. The current categories are:

    Audio
    Compressed
    Document
    Image
    Video
    Disk
    Application
    Others (for any file types not covered by the above categories)

#How to Use

    Make sure you have Python 3 installed on your system. You can download it from the official Python website.

    Clone this repository or download the organize_files.py script.

    Open your Admin terminal/command prompt.

    Change directory to where the organize_files.py script is located. For example, if it's in your Downloads folder:
    cd ~/Downloads

    Run the script with the target directory as a command line argument. For example, if you want to organize files in a directory called MyFiles on your desktop:
    python3 organize_files.py ~/Desktop/MyFiles.You just have to run it once on the command line interface , this will add "Sort Files" as an option in the context menu which will enable you to execute the command 
    on any other directory when you right click on the directory's background. 


    The script will organize the files in the specified directory into subdirectories based on their file types.

#Note

This script is currently intended to be used on systems with Python 3 installed and supporting the command line arguments format provided in the usage section. Be careful while providing the directory path, a wrong path could lead to FileNotFoundError and dont forget to BACKUP your registry. Im also working on improving it and making it more customizable.
