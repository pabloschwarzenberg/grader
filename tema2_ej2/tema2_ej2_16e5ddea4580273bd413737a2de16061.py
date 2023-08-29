def amigos(a,b):
    divisor_a=[]
    divisor_b=[]
    suma_a=0
    suma_b=0
    for i in range(1,a):
        if a%i==0:
            suma_a=suma_a+i
    for xd in range(1,b):
        if b%xd==0:
            suma_b=suma_b+xd
    if suma_a==b:
        return True
    else:
        return False
    if suma_b==a:
        return True
    else:
        return False

