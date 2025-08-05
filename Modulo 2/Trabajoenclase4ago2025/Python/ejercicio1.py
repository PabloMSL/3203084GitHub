print("\n***********************************************************************")
print("*                                                                     *")
print("* Esta es una calculadora, Por favor inserte los numeros a operar     *")
print("* Inserte el primer numero                                            *")
print("*                                                                     *")
print("* Programa hecho por Juan Mozuca                                      *")
print("*                                                                     *")
print("***********************************************************************")
numero1 = int(input())

print("\n***********************************************************************")
print("*                                                                     *")
print("* Esta es una calculadora, Por favor inserte los numeros a operar     *")
print("* Inserte el segundo numero                                           *")
print("*                                                                     *")
print("* Programa hecho por Juan Mozuca                                      *")
print("*                                                                     *")
print("***********************************************************************")
numero2 = int(input())

if numero1 == 0 or numero2 == 0 :
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    print("\n*******************************************************")
    print("*                                                     *")
    print("* La suma de sus operaciones es:                      *")
    print("*                                                     *")
    print(f"* Suma = {numero1} + {numero2} = {suma}                                    *")
    print("*                                                     *")
    print(f"* Resta = {numero1} - {numero2} = {resta}                                   *")
    print("*                                                     *")
    print(f"* Multiplicaciòn = {numero1} * {numero2} = {multi}                          *")
    print("*                                                     *")
    print(f"* Divisiòn = Error No se puede dividir entre 0        *")
    print("*                                                     *")
    print("* Programa hecho por Juan Mozuca                      *")
    print("*                                                     *")
    print("*******************************************************")

else :
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    div = numero1 / numero2
    print("\n*******************************************************")
    print("*                                                     *")
    print("* La suma de sus operaciones es:                      *")
    print("*                                                     *")
    print(f"* Suma = {numero1} + {numero2} = {suma}                                    *")
    print("*                                                     *")
    print(f"* Resta = {numero1} - {numero2} = {resta}                                   *")
    print("*                                                     *")
    print(f"* Multiplicaciòn = {numero1} * {numero2} = {multi}                          *")
    print("*                                                     *")
    print(f"* Divisiòn = {numero1} / {numero2} = {div}                              *")
    print("*                                                     *")
    print("* Programa hecho por Juan Mozuca                      *")
    print("*                                                     *")
    print("*******************************************************")


