lista = ["juan", "Sebastian", "nicolas", "Pablo", "David", "Mateo", "DIEGO"]  
lista2 = [1,2,5,7,9,8,10,12,15,20,30]
lista[6] = "pepe"
lista.append ("juan luis")
lista.insert (6, "emiliano")
lista.extend (["jose", "carlos", "karen"])
lista.remove ("Sebastian")
lista.pop (3)
lista.clear()

print(lista)
print(lista2) 
print(lista[0:7])
for i in lista:
    print(i)

