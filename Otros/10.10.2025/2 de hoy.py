#Random es una libreria q se usa para hacer las cosas de forma aleatoria
import random as rd
lista = ["Mat", "Jose", "Mateo", "Paz", "Local"]
print(rd.random())
print(rd.randint(10, 20))
print(rd.choice(lista))
print(rd.shuffle(lista))
print(rd.uniform(23, 80))