#Números Perfectos
def numero_perfecto(a):
    i = 1
    divisores = []
    while i<a:
        if a%i == 0:
            divisores.append(i)
        i = i + 1
    suma = 0
    for j in divisores:
        suma = suma + j
    if suma == a:
        return True
    else:
        return False          