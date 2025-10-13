#numpy es una libreria que se usa para operaciones matematicas, se descarga por medio de pip
import numpy as np
vector = np.array([1, 2, 3, 4, 5])
print("Vector:", vector)

suma = np.sum(vector)
media = np.mean(vector)
print("Suma del Vector", suma)
print("Media del Vector", media)

matriz = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("Matriz original\n", matriz)

transpuesta = np.transpose(matriz)
print("Matriz transpuesta\n", transpuesta)

multiplicacion = np.dot(matriz, transpuesta)
print("Multiplicacion\n", multiplicacion)