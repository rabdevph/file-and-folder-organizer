'''
• create readme.md file for instruction
• rename variables
• rename main file
• fix path - DOWNLOADS folder
'''
import shutil
import logging
from pathlib import PurePath
from pathlib import Path

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def move_file(data_dict, extension, file_item, file_name, new_path):
    '''Check file then move it to proper directory.'''
    # extension - file extension
    # file_item - file
    for category, extensions in data_dict.items():
        if extension in extensions:
            # Move item(file/s) to its proper directory.
            shutil.move(file_item, new_path / f'{category.upper()}')
            logging.info(f"[{file_name}] MOVED TO {new_path / f'{category.upper()}'}.")

        
        if extension not in extension:
            # Move to OTHER directory.
            shutil.move(file_item, new_path / 'OTHER')
            logging.info(f"[{file_item}] MOVED TO {new_path / 'OTHER'}.")
        


directory_path = Path.home() / 'Desktop' / 'Downloads'

items_dict = {
    'folder': ['FOLDER', 'AUDIO', 'COMPRESSED', 'DATABASE', 'EXE', 'IMAGE',
                 'OTHER', 'SPREADSHEET', 'TEXT', 'VIDEO',],
    'audio': ['.m4a', '.flac', '.mp3', '.wav', '.wma', '.aac'],
    'compressed': ['.zip', '.rar'],
    'database': ['.csv', '.db', '.log', '.mdb', '.sql', '.xml'],
    'exe': ['.exe', '.bat', '.msi', '.apk', '.bin', '.wsf'],
    'image': ['.jpg', '.jpeg', '.gif', '.tiff', '.psd', '.eps', '.ai', '.indd', '.raw'],
    'spreadsheet': ['.ods', '.xls', '.xlsm', '.xlsx'],
    'text': ['.doc', '.docx', '.odt', '.pdf', '.rtf', '.tex', '.txt', '.wpd'],
    'video': ['.mp4', '.mov', '.avi', '.flv', '.mkv', '.wmv', '.avchd', '.webm'],
    }

# Check if folder/s is existing. 
for folder in items_dict['folder']:
    # If not existing, create/make.
    if not (directory_path / folder).is_dir():
        Path(directory_path / folder).mkdir()
        logging.info(f"[{folder}] DIRECTORY CREATED IN {directory_path}")

items_in_folder = list(directory_path.glob('*'))
for item in items_in_folder:
    # Item is folder/directory.
    if item.is_dir():
        folder_name = PurePath(item).name
        # Check item(folder/directory) is not in items['folders'].
        if folder_name not in items_dict['folder']:
            # Move item(folder/directory) to 'FOLDERS'.
            shutil.move(item, directory_path / 'FOLDER')
            logging.info(f"{folder_name} MOVED TO {directory_path / 'FOLDER'}.")
            
    # Item is file.
    elif item.is_file():
        name_of_file = Path(PurePath(item).name)
        file_extension = name_of_file.suffix

        move_file(items_dict, file_extension, item, name_of_file, directory_path)
