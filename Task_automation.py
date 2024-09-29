import os
import shutil

# Define the directory path
directory_path = '/Users/bannu/Documents/568'

# Define the file types and their corresponding folders
file_types = {
    'documents': ['.pdf', '.docx', '.txt', '.doc'],
    'images': ['.jpg', '.png', '.gif', '.bmp', '.jpeg'],
    'videos': ['.mp4', '.avi', '.mov', '.mkv', '.wmv'],
    'audio': ['.mp3', '.wav', '.ogg', '.flac', '.aac']
}

# Create the folders if they don't exist
for folder in file_types.keys():
    folder_path = os.path.join(directory_path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files into their corresponding folders
for file in os.listdir(directory_path):
    file_path = os.path.join(directory_path, file)
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(file)[1].lower()
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                shutil.move(file_path, os.path.join(directory_path, folder, file))
                print(f"Moved {file} to {folder} folder")
                break
    elif os.path.isdir(file_path):
        print(f"Skipping directory: {file}")