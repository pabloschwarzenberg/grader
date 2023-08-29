#Suma de los N primeros números
N= int(input( " Ingrese número N : " ))
total= 0

for i in range(0, N+1):
    total = total+i
print(" La suma de los n numeros naturales de {} es: {}".format( N,total))      