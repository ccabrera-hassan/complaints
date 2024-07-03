import pandas as pd
import time
from  data_load.load import process_chunk

def process_file(new_file, column_dtypes,parse_dates):
    """ 
        Función que le el archivo por chunk
        """
    try: 
        num_chung = 0;
        
        for chunk in pd.read_csv(new_file, dtype=column_dtypes, parse_dates=parse_dates, chunksize=1000):
            inicio_carga = time.time()
            num_chung= num_chung +1;
            if not(process_chunk(chunk , num_chung)):
                  return False     
            fin_carga = time.time()    
            tiempo_total = fin_carga - inicio_carga
            print(f'Tiempo de carga del chunk {num_chung} : {tiempo_total} segundos')
        return True
    except Exception as e:
               e_m = f"Data_Extract:Process_file Chunk {num_chung}"
               print(f'{e_m} Exeption: {e}')
               return False


    

    