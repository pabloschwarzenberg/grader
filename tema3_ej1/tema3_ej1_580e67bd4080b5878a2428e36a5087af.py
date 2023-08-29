#Retorna True si es primo False si no lo es 
def suma_divisores(a):
    suma_divisores = 0
    for divisor in range(1,a):
        if a/divisor==int(a/divisor):
            suma_divisores += divisor
    if suma_divisores != 1:        
        return suma_divisores, False 
    return suma_divisores, True
if __name__=='__main__':
    print(suma_divisores(1))
    print(suma_divisores(2))
    print(suma_divisores(4))
    print(suma_divisores(7))
    print(suma_divisores(21))
    print(suma_divisores(53))
