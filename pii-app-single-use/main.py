from datetime import datetime
import time
import os
import shutil
import glob

XML_FILE_PATH = "D:\\Λήψεις\\Planet PII*.xml"
XML_FILE_DEST_PATH = 'C:\\Users\\fotic\\Desktop\\PII 4.12 v2021.102\\TaxFree Files\\{}'
XML_COMMAND = 'C:\\Users\\fotic\\Desktop\\PII 4.12 v2021.102'


if __name__ == "__main__":
    try:
        file_paths = glob.glob(XML_FILE_PATH)
        if file_paths:
            for file_path in file_paths:
                if os.path.exists(file_path):
                    time.sleep(1)
                    new_name = '{}.xml'.format(datetime.now().strftime('%d-%m-%Y_%H-%M-%S'))
                    shutil.move(file_path, XML_FILE_DEST_PATH.format(new_name))
                    time.sleep(1)
                    os.chdir(XML_COMMAND)
                    os.system('PII.exe -Refund:ALL -FileName:{}'.format(new_name))
    except FileNotFoundError:
        pass
