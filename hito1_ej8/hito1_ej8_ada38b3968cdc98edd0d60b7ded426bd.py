#Entrada
numero = int(input("Ingrese un Numero de hasta 4 digitos: "))
numero = str(numero)
#Proceso
unidad = numero[3] 
decena = numero[2] 
centena = numero[1] 
mil = numero[0] 
int(numero)
#Salida
print("{} + {} + {} + {}".format(mil + "M",centena + "C",decena + "D",unidad +"U"))