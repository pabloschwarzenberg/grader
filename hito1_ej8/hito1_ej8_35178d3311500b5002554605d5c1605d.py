#Descomponer un número
 #Descomponer un número
n = int(input("Ingrese un numero de hasta 4 digitos"))
milesima = str(n//1000) + str("M")
centesima = str(n//100 -((n//1000)*10)) + str("C")
decima = str((n%100)//10) + str("D")
unidad = str(n%10) + str("U")
if n//1000 > 0:
    print(str(milesima)+ " + " + str(centesima)+ " + " + str(decima) + " + " + str(unidad))

if n < 1000 and n > 100:
    print(str(centesima)+ " + " + str(decima) + " + " + str(unidad))

if n < 100 and n >10:
    print(str(decima) + " + " + str(unidad))

if n < 10:
    print(str(unidad))     