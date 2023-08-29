#Suma de los N primeros números
n = int(input("Calcular la suma de N numeros naturales: "))
suma = n*(n+1)/2

if n > 0:
    print(suma)
else:
    print('ingrese un numero natural')
    print(n)