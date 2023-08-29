numero = int()

def numero_perfecto(numero):
    divisor = 1
    sumadivisores = 0

    while divisor < numero:
        if numero % divisor == 0:
            sumadivisores = sumadivisores + divisor
            divisor += 1
        else:
            divisor += 1

    if sumadivisores==numero:
        return True
    else:
        return False

