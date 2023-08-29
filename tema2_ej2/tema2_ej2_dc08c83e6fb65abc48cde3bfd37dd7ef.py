def amigos(a,b):
    divisor=1
    suma_a=0
    suma_b=0
    while divisor<a:
        if a%divisor==0:
            suma_a=divisor+suma_a
        divisor=divisor+1
    divisor=1
    while divisor<b:
        if int(b)%divisor==0:
            suma_b=divisor+suma_b
        divisor=divisor+1
    if suma_a==b and suma_b==a:
        return True
    else:
        return False
print(amigos(220,284))