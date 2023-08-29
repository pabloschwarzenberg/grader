def numero_perfecto(a):
    suma = 0
    for i in range(1,a):
        #si i es divisor de a
        if a%i == 0:
            suma += i
    if suma == a:
        return True
    else:
        return False
           