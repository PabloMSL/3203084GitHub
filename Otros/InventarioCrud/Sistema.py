print("=== SISTEMA DE INVENTARIO ===")
print("1. Añadir producto")
print("2. Listar productos")
print("3. Buscar producto")
print("4. Actualizar producto")
print("5. Eliminar producto")
print("0. Salir")

opcion = input("Elija una opción: ")

if opcion == "1":
    id_ = input("Ingrese ID: ")
    nombre = input("Ingrese nombre: ")
    precio = input("Ingrese precio: ")
    stock = input("Ingrese stock: ")

    Archivo = open("inventario.txt","a")
    Archivo.write(id_ + "," + nombre + "," + precio + "," + stock + "\n")
    Archivo.close()
    print("Producto guardado.")

elif opcion == "2":
    try:
        Archivo = open("inventario.txt","r")
        lineas = Archivo.readlines()
        Archivo.close()

        if len(lineas) == 0:
            print("Inventario vacío.")
        else:
            for numero, linea in enumerate(lineas,1):
                dato = linea.strip().split(",")
                print(f"{numero}. ID:{dato[0]} - {dato[1]} - Precio:{dato[2]} - Stock:{dato[3]}")

    except:
        print("No existe archivo inventario.")

elif opcion == "3":
    print("=== SISTEMA DE INVENTARIO ===")
    print("1. Ordenar productos en base a id")
    print("2. Buscar productos en base a nombre")
    opcion = input("Elija una opción: ")

    if opcion == "2" :
     buscar = input("Ingrese ID o nombre a buscar: ")
     Archivo = open("inventario.txt","r")
     lineas = Archivo.readlines()
     ordenado = sorted(lineas)
     Archivo.close()
 
     encontrado = False
     for linea in lineas:
        dato = linea.strip().split(",")
        if buscar == dato[0] or buscar.lower() in dato[1].lower():
            print(f"Encontrado: {dato[0]} - {dato[1]} - ${dato[2]} - Stock:{dato[3]}")
            encontrado = True
     if not encontrado:
        print("Producto no encontrado.")
    elif opcion == 1:
        Archivo = open("inventario.txt","r")
        lineas = Archivo.readlines()
        ordenado = sorted(lineas)
        Archivo.close()

        for i in ordenado :
            print(i)
     

elif opcion == "4":
    Archivo = open("inventario.txt","r")
    lineas = Archivo.readlines()
    Archivo.close()

    for numero, linea in enumerate(lineas,1):
        dato = linea.strip().split(",")
        print(f"{numero}. {dato[0]} - {dato[1]}")

    seleccion = int(input("Número de producto a actualizar: "))
    datos_actuales = lineas[seleccion-1].strip().split(",")

    print("Editando:", datos_actuales)

    nuevo_precio = input("Nuevo precio: ")
    nuevo_stock = input("Nuevo stock: ")

    lineas[seleccion-1] = datos_actuales[0] + "," + datos_actuales[1] + "," + nuevo_precio + "," + nuevo_stock + "\n"

    Archivo = open("inventario.txt","w")
    Archivo.writelines(lineas)
    Archivo.close()
    print("Producto actualizado.")

elif opcion == "5":
    Archivo = open("inventario.txt","r")
    lineas = Archivo.readlines()
    Archivo.close()

    for numero, linea in enumerate(lineas,1):
        dato = linea.strip().split(",")
        print(f"{numero}. {dato[0]} - {dato[1]}")

    seleccion = int(input("Producto a eliminar: "))
    dato_borrar = lineas[seleccion-1].strip().split(",")
    print("Se va a borrar:", dato_borrar[1])

    del lineas[seleccion-1]

    Archivo = open("inventario.txt","w")
    Archivo.writelines(lineas)
    Archivo.close()
    print("Producto eliminado.")
