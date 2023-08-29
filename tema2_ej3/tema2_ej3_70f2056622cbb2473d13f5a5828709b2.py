def numero_perfecto(num):
    suma_divisores = 0

def numero_perfecto(a):
    suma_divisores = 0
    for i in range(1, a):
        if a % i == 0:
            suma_divisores += i
    if suma_divisores == a:
        return True
    else:
        return False