import pandas as pd
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from  data_extract.extract import process_file
import shutil
import os 

column_dtypes = {
    "Product": "str",
    "Issue ": "str",
    "Sub-issue": "str",
    "Consumer complaint narrative": "str",
    "Company public response": "str",
    "Company": "str",
    "State": "str",
    "ZIP code": "str",
    "Tags": "str",
    "Consumer consent provided?": "str",
    "Submitted via ": "str",
    "Company response to consumer": "str",
    "Timely response?": "str",
    "Consumer disputed? ": "str",
    "Complaint ID ": "str" 
	

}

# Especifica las columnas de fecha usando parse_dates
parse_dates = ['Date received','Date sent to company' ]



class FileHandler(FileSystemEventHandler):
    """ 
        Clase para manejar eventos de cambio de archivos
        """
    def on_created(self, event):
        """ 
        Funcion que esta evaluando si llegan nuevos archivos y dispara el procesamiento
        """
        if event.is_directory:
            return
        elif event.event_type == 'created':
            # Nuevo archivo creado, procesarlo
            time.sleep(5)  # Espera 5 segundos antes de procesar el archivo
            new_file = event.src_path
            processed_dir = os.path.join('.', 'File', 'processed')
            error_dir = os.path.join('.', 'File', 'error')
            
            if process_file(new_file, column_dtypes, parse_dates):
                shutil.move(new_file, processed_dir)
                print("Archivo movido con éxito a la carpeta processed.")
            else:
                shutil.move(new_file, error_dir)
                print("Archivo movido con éxito a la carpeta error.")





def start_monitoring(directory):
    """ 
        Función para iniciar el monitoreo del directorio
        """
    observer = Observer()
    event_handler = FileHandler()
    observer.schedule(event_handler, directory, recursive=False)
    observer.start()
    print(f'Monitoreando el directorio: {directory}')
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

