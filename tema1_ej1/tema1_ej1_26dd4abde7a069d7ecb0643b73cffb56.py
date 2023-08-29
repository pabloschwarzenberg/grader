#Suma de los N primeros números
# utilizando la función N(N+1)/2
n = int(input("ingrese el nuemro"))
num = (n * (n + 1) / 2)
suma = 0
for i in range(1,n + 1):
    suma += i

suma = sum(range(1, n + 1))
# utilizando un bucle recorriendo todos los valores y sumandolos

print(suma)      