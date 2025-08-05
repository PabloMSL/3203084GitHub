#5 diccionarios de 5 alumnos y 5 notas de cada alumno y sacar su promedio

alumno1 = {"Nombre": "Pablo", "n1": 5, "n2": 4.5, "n3": 4, "n4": 1, "n5": 2.5}
alumno2 = {"Nombre": "Johan", "n1": 5, "n2": 4.5, "n3": 4, "n4": 5, "n5": 2.5}
alumno3 = {"Nombre": "Elsanti", "n1": 5, "n2": 3.5, "n3": 3.5, "n4": 5, "n5": 3.5}
alumno4 = {"Nombre": "Valentina", "n1": 4, "n2": 5, "n3": 2.2, "n4": 4, "n5": 2.5}
alumno5 = {"Nombre": "Yusbleidy", "n1": 1, "n2": 2.5, "n3": 3, "n4": 1, "n5": 2.5}


suma1 = (alumno1["n1"] + alumno1["n2"] + alumno1["n3"] + alumno1["n4"] + alumno1["n5"])
promedio1 = suma1/5

suma2 = (alumno2["n1"] + alumno2["n2"] + alumno2["n3"] + alumno2["n4"] + alumno2["n5"])
promedio2 = suma2/5

suma3 = (alumno3["n1"] + alumno3["n2"] + alumno3["n3"] + alumno3["n4"] + alumno3["n5"])
promedio3 = suma3/5

suma4 = (alumno4["n1"] + alumno4["n2"] + alumno4["n3"] + alumno4["n4"] + alumno4["n5"])
promedio4 = suma4/5

suma5 = (alumno5["n1"] + alumno5["n2"] + alumno5["n3"] + alumno5["n4"] + alumno5["n5"])
promedio5 = suma5/5



print(alumno1["Nombre"], "Promedio:", promedio1)

print(alumno2["Nombre"], "Promedio:", promedio2)

print(alumno3["Nombre"], "Promedio:", promedio3)

print(alumno4["Nombre"],  "Promedio:", promedio4)

print(alumno5["Nombre"],  "Promedio:", promedio5)
