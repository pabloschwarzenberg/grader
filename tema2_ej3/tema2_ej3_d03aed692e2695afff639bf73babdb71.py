def numero_perfecto(a):
    suma = 0
    for divisores in range(1,a+1):
        if a % divisores == 0:
            suma += divisores
    suma -= a
    if suma == a:  
        return True
    else:
        return False

           