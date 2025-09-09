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
var1 = input("Ingrese su nombre: ")
var2 = int(input("Ingrese su edad: "))
cursor.execute("INSERT INTO usuario (nombre, edad) VALUES (%s, %s);", (var1, var2))
Conn.commit()
cursor.close()
Conn.close()