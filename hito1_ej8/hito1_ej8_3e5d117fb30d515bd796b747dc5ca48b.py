# Descomponer un número
def sep(x):
    mil = x // 1000
    n = x % 1000
    centena = n // 100
    n = n % 100
    decena = n // 10
    n = n % 10
    unidad = n
    if x >= 1000:
        descomposición = str(mil) + " M + " + str(centena) + " C + " + str(decena) + " D + " + str(unidad) + " U"
        return descomposición
    elif 1000 > x >= 100:
        descomposición = str(centena) + " C + " + str(decena) + " D + " + str(unidad) + " U"
        return descomposición
    elif 100 > x >= 10:
        descomposición = str(decena) + " D + " + str(unidad) + " U"
        return descomposición
    else:
        descomposición = str(unidad) + " U"
        return descomposición


n1 = int(input())
texto = sep(n1)
print(texto)