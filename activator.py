import time
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        print('NEW MESSAGE')
        # if "foo.txt" in event.src_path:  # in this example, we only care about this one file
        #     print("changed")


observer = Observer()
observer.schedule(Handler(), "/Users/emileberhard/Library/Messages/")  # watch the local directory
observer.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()

observer.join()
