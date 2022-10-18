import shutil
import logging
from pathlib import PurePath
from pathlib import Path

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

directory_path = Path.home() / 'Desktop' / 'Downloads'

# print(directory_path.is_dir())  # check if directory is existing

items = {
    'folders': ['DATABASES', 'EXES', 'FOLDERS', 'IMAGES',
                'SPREADSHEETS', 'OTHERS', 'TEXTS', 'VIDEOS', 'ZIPS'],
    'is_exe': True,
    'audio': ['.m4a', '.flac', '.mp3', '.wav', '.wma', '.aac'],
    'video': ['.mp4', '.mov', '.avi', '.flv', '.mkv', '.wmv', '.avchd', '.webm'],
    'image': ['.jpg', '.jpeg', '.gif', '.tiff', '.psd', '.eps', '.ai', '.indd', '.raw'],
    'text': ['.doc', '.docx', '.odt', '.pdf', '.rtf', '.tex', '.txt', '.wpd'],
    'spreadsheet': ['.ods', '.xls', '.xlsm', '.xlsx'],
    'zip': ['.zip', '.rar'],
    }

# Check if folder/s is existing. 
for folder in items['folders']:
    # If not existing, create/make.
    if not (directory_path / folder).is_dir():
        Path(directory_path / folder).mkdir()
        logging.info(f"{folder} directory created in {directory_path}")

items_in_folder = list(directory_path.glob('*'))
for item in items_in_folder:
    # Item is folder/directory.
    if item.is_dir():
        folder_name = PurePath(item).name
        # Check item(folder/directory) is not in items['folders'].
        if folder_name not in items['folders']:
            # Move item(folder/directory) to FOLDERS
            shutil.move(item, directory_path / 'FOLDERS')
            logging.debug(f"{folder_name} FOLDER MOVED TO {directory_path / 'FOLDERS'}")
            
    # Check the rest of the file/s in folder..
