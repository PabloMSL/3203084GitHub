print("Esta es una calculadora por favor eliga una opcion")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4: Division")
print("5. Potenciacion")
print("6. Exponenciacion")
print("7. Salir")
rta = int(input())
lista1 = [1,2,3,4]

if  rta == lista1[0]:
     print("Por favor inserte dos numeros")
     a = int(input())
     b = int(input())
     suma = a + b
     print(f"La suma de {a} + {b} es igual a {suma}")
    
elif rta == 2:
     print("Por favor inserte dos numeros")
     a = int(input())
     b = int(input())
     resta = a - b
     print(f"La resta de {a} - {b} es igual a {resta}")
elif rta == 3:
       print("Por favor inserte dos numeros")
       a = int(input())
       b = int(input())
       multi = a * b
       print(f"La multiplicacion de {a} * {b} es igual a {multi}")
elif rta == 4:
        print("Por favor inserte dos numeros")
        a = int(input())
        b = int(input())
        div = a / b
        print(f"La division de {a} + {b} es igual a {div}")