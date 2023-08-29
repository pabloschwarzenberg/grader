#Descomponer un número
numero=int(input("Ingrese un número de hasta 4 dígitos: "))

mil=numero//1000
centena=numero//100 - (numero//1000) * 10
decena=numero//10 - (numero//100)*10
unidad=numero//1 - (numero//10)*10

mensajeDeSalida = str(mil)+"M" + "+" + str(centena)+"C" + "+" + str(decena)+"D" + "+" + str(unidad)+"U"

print(mensajeDeSalida)      