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
cursor.execute("SELECT * FROM usuario;")
for usuario in cursor.fetchall():
    print(f"ID: {usuario[0]}, Nombre: {usuario[1]}, edad: {usuario[2]}")
cursor.close()
Conn.close()