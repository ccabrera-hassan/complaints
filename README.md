## Instalación
 
 1. Clonar el repositorio:



git clone <url_del_repositorio>


 2. Crear y activar el ambiente virtual:


python -m venv venv
source venv/bin/activate   # En Windows usa `venv\Scripts\activate`

3. Instalar las dependencias:


pip install -r requirements.txt

4. Ejecutar Docker Compose en el directorio \bd:
cd bd
docker-compose up -d

5. Ejecutar la aplicación desde el entorno virtual:

python main.py

## Otra Opción:

1. Construir la imagen Docker en el directorio raíz del proyecto:


docker build -t myapi .

2. Iniciar el contenedor Docker:


docker run -d --name myapi-container myapi

## Funcionalidad

El proyecto procesa el archivo complaints.csv de la siguiente manera:
Descargar el archivo de complaints.csv  (https://www.kaggle.com/datasets/anoopjohny/consumer-complaint-database/data)

1. Colocar el archivo en la carpeta File/to_process.

2. Si el procesamiento es exitoso, los registros se insertan en la base de datos del contenedor Docker (docker-compose) en la tabla complaints y el archivo se mueve a File/processed.

En caso de error, el archivo se traslada a File/error.

## Mejoras Futuras

.Implementar validación para aceptar únicamente archivos .csv.

.Mejorar el monitoreo de archivos para evitar procesarlos durante la transferencia.

.Implementar control de formato y manejo de excepciones, trasladando archivos con problemas a la carpeta de error.

.Configurar niveles de logging y generación de archivo de log.

.Implementar procesamiento en paralelo utilizando hilos para insertar datos en la base de datos.

.Considerar la creación de una tabla de control en la base de datos para permitir la recuperación desde un punto específico en caso de errores durante el procesamiento por chunks.

.Se puede agregar un archivo config.ini para que tome el numero de lineas que tomaran los chunk y no este hardcodeado en el codigo, igual con el esquema del archivo y las rutas. 
