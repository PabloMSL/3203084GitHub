import psycopg2
Conn = psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "1234",
    database = "senacba",
    port = 5432
)
print(Conn)
print("Conexion EXITOSA")
cursor = Conn.cursor()
cursor.execute("CREATE TABLE usuario( id SERIAL PRIMARY KEY, nombre VARCHAR(80), edad INT);")
Conn.commit()
cursor.close()
Conn.close()
