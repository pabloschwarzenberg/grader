# Números Perfectos
# 2 points
#
# Un número se dice número perfecto, si la suma de todos sus divisores es igual
# al mismo número (No debes considerar como divisor al mismo número). Crea una
# función llamada numero_perfecto que reciba un número y retorne True si es un
# número perfecto, y False en caso de no serlo.

def divisores(num):
    div = []
    sum = 0
    for i in range(1, num - 1):
        if (num % i) == 0:
            div.append(i)
    for j in div:
        sum += j
    return sum

def numero_perfecto(num):
    sum = divisores(num)
    if num == sum:
        return True
    else:
        return False

# print(numero_perfecto(496))

           