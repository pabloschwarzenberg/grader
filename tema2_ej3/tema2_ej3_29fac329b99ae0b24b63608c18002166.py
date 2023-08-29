def numero_perfecto(a):
    suma = 0
    for i in range(1, a):
        if a % i == 0:
            suma += i
        else:
            suma = suma
    if suma == int(a):
        return True
    else:
        return False