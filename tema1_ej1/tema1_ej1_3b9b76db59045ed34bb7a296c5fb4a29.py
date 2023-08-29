#Suma de los N primeros números
n=int(input('Ingrese la cantidad de numeros naturales que desea sumar: '))

resultado=n*(n+1)/2
suma=int(resultado)
if n>=0:
    print(suma)
elif n<0:
    print('ERROR, Ingrese un numero natural.')