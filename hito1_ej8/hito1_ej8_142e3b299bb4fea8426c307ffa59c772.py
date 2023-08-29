#Descomponer un número
def descomposicion(numero):
    unidades=numero%10
    decenas=(numero//10)%10
    centenas =(numero//100)%10
    miles =(numero//1000)%10

    descomposicion= ""

    if(miles>=0):
        descomposicion += str(miles) + "M + "
    if(centenas>=0):
        descomposicion += str(centenas) + "C + "
    if(decenas>=0):
        descomposicion += str(decenas) + "D + "
    if(unidades>=0):
        descomposicion += str(unidades) + "U + "

    return descomposicion.strip().rstrip("+")

numero= int(input("Ingrese un número de hasta 4 dígitos: "))

descomposicion= descomposicion(numero)

print("La descomposición del número es:", (descomposicion))