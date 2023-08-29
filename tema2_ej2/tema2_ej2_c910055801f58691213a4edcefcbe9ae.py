# completa el código de la función
def amigos(a, b):
    if a == b:
        return False

    suma1 = 0
    suma2 = 0

    for num in range(1, int(a / 2)+1):
        if a % num == 0:
            suma1 += num


    for num2 in range(1, int(b / 2)+1):
        if b % num2 == 0:
            suma2 += num2


    if suma1 == b and suma2== a:
        return True

    return False

           