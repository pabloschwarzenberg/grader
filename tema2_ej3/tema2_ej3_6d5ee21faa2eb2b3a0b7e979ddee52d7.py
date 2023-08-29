def numero_perfecto(n):
    suma = 0
    for number in range(1,n):
        if n % number == 0 :
            suma = number + suma
    if suma == n :
        return True
    else :
        return False
           