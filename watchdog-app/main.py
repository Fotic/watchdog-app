from datetime import datetime
import time
import os
import shutil
import watchdog.events
import watchdog.observers
import glob


OBSERVER_PATH = "D:\\Λήψεις"

PDF_FILE_PATH = 'D:\\Λήψεις\\Order Receipt*.pdf'
PDF_FILE_DEST_PATH = 'D:\\printspdf\\{}'

PDF_FILE_PATH2 = 'D:\\Λήψεις\\Τιμολόγιο - ΑΛΠW*.pdf'
PDF_FILE_DEST_PATH2 = 'D:\\printsxml\\{}'

XML_FILE_PATH = "D:\\Λήψεις\\Planet PII*.xml"
XML_FILE_DEST_PATH = 'C:\\Users\\fotic\\Desktop\\PII 4.12 v2021.102\\TaxFree Files\\{}'
XML_COMMAND = 'C:\\Users\\fotic\\Desktop\\PII 4.12 v2021.102'

class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=[
            'Order Receipt*.pdf',
            'Planet PII*.xml',
            'Τιμολόγιο - ΑΛΠW*.pdf'
        ],ignore_directories=True, case_sensitive=False)

    def call_move_file(self,event):
        time.sleep(2)

        try:
            file_paths = glob.glob(PDF_FILE_PATH)
            if file_paths:
                print(file_paths)
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
                print(file_paths)
                for file_path in file_paths:
                    if os.path.exists(file_path):
                        time.sleep(1)
                        new_name = '{}.pdf'.format(datetime.now().strftime('%d-%m-%Y_%H-%M-%S'))
                        shutil.move(file_path, PDF_FILE_DEST_PATH2.format(new_name))
        except FileNotFoundError:
            pass

        try:
            file_paths = glob.glob(XML_FILE_PATH)
            if file_paths:
                print(file_paths)
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


    def on_created(self, event):
        self.call_move_file(event)

    def on_modified(self, event):
        self.call_move_file(event)


if __name__ == "__main__":
    src_path = OBSERVER_PATH
    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
