def amigos(a,b):
    Suma_divisor_1=0
    Suma_divisor_2=0
    for x in range(1,a) :
        if a % x == 0 :
            Suma_divisor_1+=x
    for y in range(1,b) :
        if b % y == 0 :
            Suma_divisor_2+=y
    if Suma_divisor_1 ==  b and Suma_divisor_2==a:
        return True
    else :
        return False