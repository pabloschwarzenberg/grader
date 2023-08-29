#Suma de los N primeros números
#entradas 
n = int(input("ingrese el numero natural: "))

suma = n * (n+1)/2
#desarrollo 
suma = sum(range(1, n + 1))

print(suma)
 
