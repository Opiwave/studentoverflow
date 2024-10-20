from sqlalchemy import create_engine

# Cambia aquí la cadena de conexión si es necesario
DATABASE_URL = 'postgresql://postgres:caguai69@localhost/proyectofinal'

try:
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    print("Conexión exitosa a la base de datos.")
    connection.close()
except Exception as e:
    print(f"Ocurrió un error al conectar a la base de datos: {e}")
