#Suma de los N primeros números
n = int(input("ingresa hasta que numero natural se realizara el calculo: "))

while n < 0:
    n = int(input("ingrese un numero natural: "))
print(" el resultado es: ",n*(n+1)/2)