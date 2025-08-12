def crear_lista_input():
      entrada = input("Ingrese los elementos de la lista separados por comas: ")
      elementos = entrada.split(",")
      return [elemento.strip() for elemento in elementos]

print("Esta es una calculadora de listas por favor eliga una opcion")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4: Division")
print("5. Salir")
rta = crear_lista_input()

if  rta[0] == "1":
     print("Por favor inserte dos listas")
     lista1 = crear_lista_input()
     lista2 = crear_lista_input()
     listasuma = lista1 + lista2
     print(f"La suma de {lista1} + {lista2} es igual a {listasuma}")
    
elif rta[0] == "2":
       print("Por favor inserte dos listas")
       lista1 = crear_lista_input()
       lista2 = crear_lista_input()
       listasresta = lista1 - lista2
       print(f"La suma de {lista1} + {lista2} es igual a {listaresta}")
  
elif rta[0] == "3":
       print("Por favor inserte una lista y por cuanto lo quiere concatenar")
       lista1 = crear_lista_input()
       b = int(input())
       multi = lista1 * b
       print(f"La multiplicacion de {lista1} * {b} es igual a {multi}")
elif rta[0] == "4":
        print("Por favor inserte dos numeros")
        a = int(input())
        b = int(input())
        div = a / b
        print(f"La division de {a} + {b} es igual a {div}")