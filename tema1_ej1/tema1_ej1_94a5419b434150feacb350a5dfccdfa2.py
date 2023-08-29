#Suma de los N primeros números

a = int(input("Ingrese un número que sea natural : "))
while a<0:
    a = int(input("Ingrese un número que sea perteneciente a los naturales: "))
    

b= a*(a + 1)/2
print("Suma de los N primeros números es:", b)