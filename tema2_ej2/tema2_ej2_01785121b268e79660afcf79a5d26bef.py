# completa el código de la función
def amigos(a,b):
    suma_divisor_1=0
    suma_divisor_2=0
    for x in range(1,a) :
        if a % x == 0 :
            suma_divisor_1+=x
    for y in range(1,b) :
        if b % y == 0 :
            suma_divisor_2+=y
    if suma_divisor_1 == b and suma_divisor_2==a:
        return True
    else :
        return False
           