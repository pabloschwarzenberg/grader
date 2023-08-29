def numero_perfecto(x):
    suma = 0

    for i in range(1, x):
        if x % i == 0:
            suma = suma + i
    if suma == x:
        return True

    return False

           