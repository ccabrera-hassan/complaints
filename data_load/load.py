import pandas as pd
from sqlalchemy import create_engine
from utils.db import engine
from data_transform.transform import transform_chunk





def process_chunk(chunk , num_chung):
        """ 
        Función que aplica las tranformaciones e inserta en la base de datos
        """
        try:  
        
            tr_chunk = transform_chunk(chunk)

        # Insertar lotes de datos en la base de datos
            tr_chunk.to_sql(name='complaints', con=engine, if_exists='append', index=False)
            print(f'Chunk procesado exitosamente: {num_chung}')

            return True

        except Exception as e:
                e_m = f"Data_Load:Process_chunk chunk {num_chung}"
                print(f'{e_m} Exeption: {e}')
                return False
