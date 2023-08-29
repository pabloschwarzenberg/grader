#Descomponer un número
#ENTRADA
numero = input("ingrese un numero que tenga entre 1 y 4 cifras: ")

#PROCESO
#unidades decenas centenas miles
UDCM = "UDCM"
i = len(numero)-1
descomposicion =""
#bucle que generara la descomposicion y la almacenara en una nueva string
while ( i >= 0):
    #si ya se agrego el primer numero, empieza a poner los +
    if (i <= (len(numero)-2)):
        descomposicion += " + "
    #se agregan los numeros y las unidades a la string
    descomposicion += (numero[-i-1]+UDCM[i])
    i-=1

#SALIDA
print(descomposicion)
      