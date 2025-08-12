lista = ["suma","resta","division","multiplicacion"]
ingresar = int(input("Ingrese un numero, 1. Suma , 2. Resta , 3. Division o 4. Multiplicacion "))
print("Ahora ingrese los dos numeros para operar")
a = int(input())
b = int(input())

if ingresar == 1:
    print(lista[0])
    print(a+b) 
elif ingresar == 2:
    print(lista[1])
    print(f"La resta de los dos numeros es: {a-b}")
elif ingresar == 3:
    print(lista[2])
    print(a*b)
elif ingresar == 4:
    print(lista[3])
    print(a/B)
