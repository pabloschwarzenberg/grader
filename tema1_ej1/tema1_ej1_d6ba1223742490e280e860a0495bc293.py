#Suma de los N primeros números
n = int(input("Ingrese un numero: "))

suma=0
ind = 1
while ind <= n:
    suma = suma + ind
    ind= ind + 1

print("la suma de los primeros ", n,"  numeros naturales es: ", suma)
