def numero_perfecto(a):
    suma = 0
    for div in range(1,a):
        if a%div == 0:
            suma = suma + div
    if suma == a: return True
    return False