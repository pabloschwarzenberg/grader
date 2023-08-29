def numero_perfecto(a):
    suma = 0
    for numero in range(1, a):
        if a % numero == 0:
            suma += numero
    if suma == a:
        return True
    else:
        return False