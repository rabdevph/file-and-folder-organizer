"""
- create readme.md file for instructions
- fix path: DOWNLOADS folder
"""
import shutil
import logging
from pathlib import PurePath
from pathlib import Path

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def move_file(formats, extension, file, folder_path):
    '''Check file then move it to designated directory.'''
    file_name = Path(PurePath(file).name)
    file_moved = False

    # Check file extension(format).
    for category, extensions in formats.items():
        if extension in extensions:
            # Move item(file/s) to its proper directory.
            shutil.move(file, folder_path / f'{category.upper()}')
            logging.info(
                f"[{file_name}] moved to {(folder_path / f'{category.upper()}').name} directory.")
            file_moved = True

    if not file_moved:
        # Move to OTHER directory.
        shutil.move(file, folder_path / 'OTHER')
        logging.info(
            f"[{file_name}] moved to {(folder_path / 'OTHER').name} directory.")


# DOWNLOADS directory path.
directory_path = Path.home() / 'Desktop' / 'Downloads'

# List for directory.
folder_list = ['FOLDER', 'AUDIO', 'COMPRESSED', 'DATABASE', 'EXE', 'IMAGE',
               'OTHER', 'SPREADSHEET', 'TEXT', 'VIDEO', ]

file_formats = {
    'audio': ['.m4a', '.flac', '.mp3', '.wav', '.wma', '.aac'],
    'compressed': ['.zip', '.rar'],
    'database': ['.csv', '.db', '.log', '.mdb', '.sql', '.xml'],
    'exe': ['.exe', '.bat', '.msi', '.apk', '.bin', '.wsf'],
    'image': ['.jpg', '.jpeg', '.gif', '.tiff', '.psd', '.eps', '.ai', '.indd', '.raw'],
    'spreadsheet': ['.ods', '.xls', '.xlsm', '.xlsx'],
    'text': ['.doc', '.docx', '.odt', '.pdf', '.rtf', '.tex', '.txt', '.wpd'],
    'video': ['.mp4', '.mov', '.avi', '.flv', '.mkv', '.wmv', '.avchd', '.webm'],
}

# Check if folder/directory exists in DOWNLOADS.
for folder in folder_list:
    if not (directory_path / folder).is_dir():
        Path(directory_path / folder).mkdir()
        logging.info(f"New directory [{folder}] created.")

# List of items in DOWNLOADS.
items_in_folder = list(directory_path.glob('*'))

# Check for items in the DOWNLOADS.
for item in items_in_folder:
    # Item is FOLDER/DIRECTORY.
    if item.is_dir():
        folder_item = PurePath(item).name
        if folder_item not in folder_list:
            # Move folder/directory to FOLDER.
            shutil.move(item, directory_path / 'FOLDER')
            logging.info(
                f"[{folder_item}] moved to {(directory_path / 'FOLDER').name} directory.")

    # Item is FILE.
    elif item.is_file():
        file_extension = Path(PurePath(item).name).suffix
        file_item = item
        # Move to proper directory.
        move_file(file_formats, file_extension, file_item, directory_path)
