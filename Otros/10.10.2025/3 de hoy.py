#genera atraves de el disco de la computadora
import dask.array as da
x = da.random.randint(1, 11, size=10, chunks=5)
print("Numeros generados:")
print(x.compute())

media = x.mean()
print("Promedio:")
print(media.compute())