# Mi primera función
def preguntar(nombre): # def define la función, nombre es el parámetro
    """Esta función saluda a una persona por su nombre"""
    mensaje = f"¡Hola {nombre}! ¿Como realizo el codigo?"
    return mensaje # return devuelve el resultado

# Usar la función (llamarla)
saludo1 = preguntar("Ana") # Llamamos la función con "Ana"
saludo2 = preguntar("Carlos") # La reutilizamos con "Carlos"
saludo3 = preguntar("María") # Y otra vez con "María"
print("Usando mi función de saludo:")
print(saludo1)
print(saludo2)
print(saludo3)
# También podemos usarla directamente
print("\nUsando directamente:")
print(preguntar("Pedro"))
print(preguntar("Laura"))