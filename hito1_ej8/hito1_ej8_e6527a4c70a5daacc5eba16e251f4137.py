#Descomponer un número
x = int(input("Ingrese un numero de 4 cifras: "))

unidad = x%10
x = x//10

decena = x%10
x = x//10

centena = x%10
x = x//10

Udemil = x%10
x = x//10
print("Descomposicion:{}M + {}C + {}D + {}U".format(Udemil, centena, decena, unidad)) 