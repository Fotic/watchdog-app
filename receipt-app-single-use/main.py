from datetime import datetime
import time
import os
import shutil
import glob


PDF_FILE_PATH = 'D:\\Λήψεις\\Order Receipt*.pdf'
PDF_FILE_DEST_PATH = 'D:\\printspdf\\{}'

PDF_FILE_PATH2 = 'D:\\Λήψεις\\Τιμολόγιο - ΑΛΠW*.pdf'
PDF_FILE_DEST_PATH2 = 'D:\\printsxml\\{}'


if __name__ == "__main__":
    try:
        file_paths = glob.glob(PDF_FILE_PATH)
        if file_paths:
            for file_path in file_paths:
                if os.path.exists(file_path):
                    time.sleep(1)
                    new_name = '{}.pdf'.format(datetime.now().strftime('%d-%m-%Y_%H-%M-%S'))
                    shutil.move(file_path, PDF_FILE_DEST_PATH.format(new_name))
    except FileNotFoundError:
        pass

    try:
        file_paths = glob.glob(PDF_FILE_PATH2)
        if file_paths:
            for file_path in file_paths:
                if os.path.exists(file_path):
                    time.sleep(1)
                    new_name = '{}.pdf'.format(datetime.now().strftime('%d-%m-%Y_%H-%M-%S'))
                    shutil.move(file_path, PDF_FILE_DEST_PATH2.format(new_name))
    except FileNotFoundError:
        pass
