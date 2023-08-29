#Suma de los N primeros números
n= int(input('ingrese un numero natural n: '))

N = n*(n + 1)/2

if 0<n:
    print('La suma de los primeros ',n,'numeros naturales es ',int(N))
elif n==0:
    print('El cero no pertenece a los numeros naturales')
elif 0>n:
    print('Los numeros negativos aparecen por primera vez en el conjunto de los numeros enteros')

      