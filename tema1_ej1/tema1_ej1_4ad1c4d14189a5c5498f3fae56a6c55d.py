#Suma de los N primeros números
def suma_naturales(elem):
    if elem <= 0: #El cero y los negativos no son naturales
        return False
    lista = []
    cont = 1
    while cont<=elem:
        lista.append(cont)
        cont = cont+1
    suma = 0
    for i in lista:
        suma = suma + i
    return suma
        
        
n = int(input())
print(suma_naturales(n))
