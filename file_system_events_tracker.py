import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir='/Users/maithreyisairam/Downloads'






class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print("hey,{event.src_path} has been created")
    def on_deleted(self,event):
        print("oh no! someone deleted {event.src_path}!")
    def on_modified(self,event):
        print("hey,{event.src_path} has been modified" )
    def on_moved(self,event):
        print("someone moved {event.src_path} to {event.dest_path}")

event_handler = FileMovementHandler()



observer = Observer()


observer.schedule(event_handler, from_dir, recursive=True)



observer.start()

try:

    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print('stop')   
    observer.stop()     


    