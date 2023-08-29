#Suma de los N primeros números
suma = 0
n = int(input("Ingrese número: "))

for i in range(1,n+1):
    suma += i
    
print(suma)