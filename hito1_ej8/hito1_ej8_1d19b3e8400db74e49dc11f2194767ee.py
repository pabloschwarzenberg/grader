#Descomponer un número
#Definir la funcion descomponer_numero
def descomponer_numero(numero):
    unidades=numero%10
    decenas=(numero//10)%10
    centenas=(numero//100)%10
    miles=numero//1000
    return miles,centenas,decenas,unidades

#Solicitar al usuario un numero de maximo 4 digitos
numero=int(input("Ingrese un numero de maximo 4 digitos: "))
miles,centenas,decenas,unidades=descomponer_numero(numero)

#Imprimir la descomposicion 
descomposicion=""
if miles>0:
    descomposicion=descomposicion+str(miles)+"M+"
if centenas>0:
    descomposicion=descomposicion+str(centenas)+"C+"
if decenas>=0:
    descomposicion=descomposicion+str(decenas)+"D+"
if unidades>=0:
    descomposicion=descomposicion+str(unidades)+"U"
print(descomposicion)      