from contextvars import ContextVar
from sqlalchemy import create_engine


from utils.settings import Settings

settings = Settings()

DB_NAME = settings.db_name
DB_USER = settings.db_user
DB_PASS = settings.db_pass
DB_HOST = settings.db_host
DB_PORT = settings.db_port

# Configuración de la conexión a la base de datos
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}')



