#Suma de los N primeros números
n=int(input('ingrese valor para n: '))

i=0
suma = n*(n+1)/2
while i<=n:
    suma=i+suma

    print('La sumatoria es igual a',suma)
    break      