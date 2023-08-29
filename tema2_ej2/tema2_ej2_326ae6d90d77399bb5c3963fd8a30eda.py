# completa el código de la función
def amigos(a,b):
    sumaDivisor_1=0
    sumaDivisor_2=0
    for x in range(1,a) :
        if a % x == 0 :
            sumaDivisor_1+=x
    for y in range(1,b) :
        if b % y == 0 :
            sumaDivisor_2+=y
    if sumaDivisor_1 ==  b and sumaDivisor_2==a:
        return True
    else :
        return False
           