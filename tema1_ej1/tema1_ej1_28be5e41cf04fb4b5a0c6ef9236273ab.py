def suma_naturales(n):
    suma = n*(n+1)/2
    return suma

numero= int(input('ingrese un numero'))

resultado= suma_naturales(numero)
print('el resultado es',numero,'numeros naturales',resultado)
