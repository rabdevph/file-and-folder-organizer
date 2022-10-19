'''
• refactor code - use functions
• create readme.md file for instruction
• rename main file
'''
import shutil
import logging
from pathlib import PurePath
from pathlib import Path

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

directory_path = Path.home() / 'Desktop' / 'Downloads'

# print(directory_path.is_dir())  # check if directory is existing

items = {
    'folders': ['FOLDERS', 'AUDIOS', 'COMPRESSED', 'DATABASES', 'EXES', 'IMAGES',
                 'OTHERS', 'SPREADSHEETS', 'TEXTS', 'VIDEOS',],
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
for folder in items['folders']:
    # If not existing, create/make.
    if not (directory_path / folder).is_dir():
        Path(directory_path / folder).mkdir()
        logging.info(f"{folder} DIRECTORY CREATED IN {directory_path}")

items_in_folder = list(directory_path.glob('*'))
for item in items_in_folder:
    # Item is folder/directory.
    if item.is_dir():
        folder_name = PurePath(item).name
        # Check item(folder/directory) is not in items['folders'].
        if folder_name not in items['folders']:
            # Move item(folder/directory) to 'FOLDERS'.
            shutil.move(item, directory_path / 'FOLDERS')
            logging.info(f"{folder_name} MOVED TO {directory_path / 'FOLDERS'}.")
            
    # Item is file.
    elif item.is_file():
        file_name = Path(PurePath(item).name)

        # Item is audio file.
        if (file_name.suffix in items['audio']):
            # Move item(file/s) to 'AUDIOS'.
            shutil.move(item, directory_path / 'AUDIOS')
            logging.info(f"{file_name} MOVED TO {directory_path / 'AUDIOS'}.")

        # Item is compressed file.
        elif (file_name.suffix in items['compressed']):
            # Move item(file/s) to 'COMPRESSED'.
            shutil.move(item, directory_path / 'COMPRESSED')
            logging.info(f"{file_name} MOVED TO {directory_path / 'COMPRESSED'}.")

        # Item is database file.
        elif (file_name.suffix in items['database']):
            # Move item(file/s) to 'DATABASES'.
            shutil.move(item, directory_path / 'DATABASES')
            logging.info(f"{file_name} MOVED TO {directory_path / 'DATABASES'}.")
        
        # Item is executable file.
        elif (file_name.suffix in items['exe']):
            # Move item(file/s) to 'EXES'.
            shutil.move(item, directory_path / 'EXES')
            logging.info(f"{file_name} MOVED TO {directory_path / 'EXES'}.")

        # Item is image file.
        elif (file_name.suffix in items['image']):
            # Move item(file/s) to 'IMAGES'.
            shutil.move(item, directory_path / 'IMAGES')
            logging.info(f"{file_name} MOVED TO {directory_path / 'IMAGES'}.")

        # Item is spreadsheet file.
        elif (file_name.suffix in items['spreadsheet']):
            # Move item(file/s) to 'SPREADSHEETS'.
            shutil.move(item, directory_path / 'SPREADSHEETS')
            logging.info(f"{file_name} MOVED TO {directory_path / 'SPREADSHEETS'}.")

        # Item is text file.
        elif (file_name.suffix in items['text']):
            # Move item(file/s) to 'TEXTS'.
            shutil.move(item, directory_path / 'TEXTS')
            logging.info(f"{file_name} MOVED TO {directory_path / 'TEXTS'}.")

        # Item is video file.
        elif (file_name.suffix in items['video']):
            # Move item(file/s) to 'VIDEOS'.
            shutil.move(item, directory_path / 'VIDEOS')
            logging.info(f"{file_name} MOVED TO {directory_path / 'VIDEOS'}.")

        # Item is other file.
        else:
            # Move item(file/s) to 'OTHERS'.
            shutil.move(item, directory_path / 'OTHERS')
            logging.info(f"{file_name} MOVED TO {directory_path / 'OTHERS'}.")
