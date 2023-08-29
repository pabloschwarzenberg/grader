#Suma de los N primeros números
n = int(input("Ingrese un numero natural "))

suma =0

for i in range(1, n+1):
    suma += i
    
print(suma)  