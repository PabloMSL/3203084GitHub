import psycopg2
Conn = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="1234",
        database="senacba",
        port=5432
)
cursor = Conn.cursor()
id_a_borrar = 3
cursor.execute("DELETE FROM usuario WHERE id = %s;", (id_a_borrar,))
Conn.commit()
print(f"Usuario con ID {id_a_borrar} eliminado correctamente")
cursor.close()
Conn.close()

