#Descomponer un número
#inicio
#pedirle al usuario que introduzca un número de cuatro cifras
num = int(input("Ingrese un número de 4 cifras: "))
#proceso divisiones y restos entre 10
aux = num
unidades = aux % 10
aux = aux //10
decenas = aux % 10
aux = aux // 10
centenas = aux % 10
umil = aux //10
#salida
print("Descomposición de ", num," : ", umil,"M +", centenas, "C +", decenas, "D +", unidades, "U " )     