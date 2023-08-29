def numero_perfecto(a):
    suma = 0
    for n in range(1,a):
        if (a % (n) == 0):
            suma += (n)
    if a == suma:
        return True
    else:
        return False 