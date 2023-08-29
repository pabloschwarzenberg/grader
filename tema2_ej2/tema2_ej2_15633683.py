def amigos(a,b):
    suma_a=1
    suma_b=1
    for i in range (2,a+1):
        if a%i==0:
            suma_a+=i
    for i in range (2,b+1):
        if b%i==0:
            suma_b+=i
    if suma_a==suma_b:
        if a==b:
            return False
        else:
            return True
    else:
        return False