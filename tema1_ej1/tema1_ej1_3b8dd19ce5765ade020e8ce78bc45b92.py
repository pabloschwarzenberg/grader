#Suma de los N primeros números
print("Ingrese un numero:")
num = int(input())
cont = 0
suma = 0
while cont <= num:
    suma = suma + cont
    cont = cont + 1
print("La suma es: ", suma)
