#Suma de los N primeros números

num = int(input("Ingrese un Número : "))
cont = 0
suma = 0
while cont <= num:
    suma += cont
    cont += 1
print("La Suma es : ",suma)