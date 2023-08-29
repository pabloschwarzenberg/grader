#Descomponer un número
numero = int(input("Ingrese numero de hasta 4 cifras: "))

miles = numero//1000
numero %= 1000

centenas = numero//100
numero %= 100

decenas = numero//10
unidades = numero%10

if miles == 0 and centenas != 0: print(centenas, "C + ", decenas, "D + ", unidades, "U")
elif miles == 0 and centenas == 0 and decenas != 0: print(decenas, "D + ", unidades, "U")
elif miles == 0 and centenas == 0 and decenas == 0: print(unidades, "U")
else: print(miles, "M + ",centenas, "C + ",decenas, "D + ", unidades, "U")