# Un número se dice número perfecto, si la suma de todos sus divisores es igual
# al mismo número (No debes considerar como divisor al mismo número). Crea una
# función llamada numero_perfecto que reciba un número y retorne True si es un
# número perfecto, y False en caso de no serlo.

def divi(numero):
    div = []
    suma = 0
    for i in range(1, numero - 1):
        if (numero % i) == 0:
            div.append(i)
    for j in div:
        suma += j
    return suma

def numero_perfecto(numero):
    suma = divi(numero)
    if numero == suma:
        return True
    else:
        return False

