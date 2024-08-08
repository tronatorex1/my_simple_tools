# This codes creates a Listener (like in PS) that detects file/fiolder events in
#   a desired path. It used watchdog as listener resource

import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

# to stop, just press ctrl + C at the Python console
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    #path = sys.argv[1] if len(sys.argv) > 1 else '.'
    path = "D:\\TMP"
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()