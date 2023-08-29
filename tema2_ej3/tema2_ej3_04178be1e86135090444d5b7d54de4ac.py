def numero_perfecto(a):
    suma = 0
    for x in range(1, a):
        if a % x == 0:
            suma = suma + x
    if a == suma:
        return True
    else:
        return False