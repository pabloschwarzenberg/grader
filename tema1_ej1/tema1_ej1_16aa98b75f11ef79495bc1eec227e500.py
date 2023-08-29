#Suma de los N primeros números
n = int(input("ingrese numero Q : "))
suman = (n * (n + 1)) / 2 

while n > 0:
    if suman > 0:
        n = n - 1
    
print("La suma es de : ",suman)







