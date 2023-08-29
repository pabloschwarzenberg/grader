#Descomponer un número
def contar_caracteres(cadena):
    contador = 0
    while cadena[contador:]:
        contador += 1
    return contador
numero = input("Ingrese un numero de hasta 4 digitos:")
digitos = (len(numero))
if digitos == 1:
    print(numero,"U")
if digitos == 2:
    D = numero[0]
    U = numero[1]
    print(D,"D","+",U,"U")
if digitos == 3:
    C = numero[0]
    D = numero[1]
    U = numero[2]
    print(C,"C","+",D,"D","+",U,"U")
if digitos == 4:
    M = numero[0]
    C = numero[1]
    D = numero[2]
    U = numero[3]
    print(M,"M","+",C,"C","+",D,"D","+",U,"U")