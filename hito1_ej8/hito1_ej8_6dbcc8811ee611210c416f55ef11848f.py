#Descomponer un número
numero = int(input("ingrese un numeeo de hasta 4 cifras: "))

#Proceso: // % numero//10 numero //100 numero %10 numeri %100
milesima = numero//1000
centenas =(numero//100)%10
decenas = (numero//10)%10
unidades = numero%10

mensaje = str(milesima) + "M +" + str(centenas) + "C + " + str(decenas) + "D + " + str(unidades) + "U"

print(mensaje)    