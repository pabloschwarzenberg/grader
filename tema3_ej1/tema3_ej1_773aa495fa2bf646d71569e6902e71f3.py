# completa el código de la función           
# Suma de los divisores de un número
# 2 points

# Crea una función que calcule la suma de los divisores de un número sin incluir
# al número, llamada suma_divisores. Junto con la suma de los divisores haz que
# la función retorne si el número es primo o no, basándose en que si la suma de
# sus divisores es 1, el número es primo.
#

def suma_divisores(num):
    div = []
    sum = 0
    for i in range(1, num - 1):
        if (num % i) == 0:
            div.append(i)
    for j in div:
        sum += j
    if sum == 1:
        return sum, True
    else:
        return sum, False
