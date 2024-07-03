from data_extract.watcher import start_monitoring
import os

# Directorio a monitorear
directory_to_watch = os.path.join('.', 'File', 'to_process')

if __name__ == "__main__":
    start_monitoring(directory_to_watch)
