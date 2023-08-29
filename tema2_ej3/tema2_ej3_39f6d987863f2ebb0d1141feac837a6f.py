def numero_perfecto(a):
    suma= 0
    for divisor in range(1,a+1):
        if (a % divisor) == 0 :
            suma += divisor
    suma= suma - a
    if suma== a:
        return True
    else: return False