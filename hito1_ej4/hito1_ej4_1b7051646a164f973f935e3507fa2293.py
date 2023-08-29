#Ingresamos el numero decimal
numero = int(input("Ingresa un numero decimal"))

#Creamos la funcion 
def decimalBinario(decimal):

    resultado = "" #Cadena que guarda el resultado

    while decimal > 0 : #Ciclo que se genera mientras decimal sea mayor a 0
        restante = decimal % 2 #Modulo 2 del numero
        resultado = resultado + str(restante) #Acumula la cadena final
        decimal = decimal // 2 #Divion entera que busca el nuevo numero para dividir

    return resultado[::-1] #Invierte el resultado

print(decimalBinario(numero))