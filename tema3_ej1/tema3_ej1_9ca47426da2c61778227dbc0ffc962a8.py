# completa el código de la función
def suma_divisores(lista, multiplo):
    suma = 0
    for numero in lista:
        if numero % multiplo == 0:
            suma += numero
    return suma

numeros1 = [1,5,4,9,6,8]
numeros2 = [2,6,5,8,2,4]
multiplo = 3

print (suma_divisores(numeros1, multiplo))
print (suma_divisores(numeros2, multiplo))


           