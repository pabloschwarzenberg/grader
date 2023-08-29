def numero_perfecto(z):
    suma = 0
    for i in range(1,z):
        if z % i == 0:
            suma += i
    return suma == z
