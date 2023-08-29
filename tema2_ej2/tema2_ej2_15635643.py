def amigos(a,b):
    divisor_a=1
    divisor_b=1
    suma_a=0
    suma_b=0
    while divisor_a<a:
        if a%divisor_a==0:
            suma_a+=divisor_a
        divisor_a+=1
    while divisor_b<b:
        if b%divisor_b==0:
            suma_b+=divisor_b
        divisor_b+=1
    if a==1 or b==1:
        return False
    elif suma_a==b or suma_b==a:
        return True
    else:
        return False
if __name__ == "__main__":
    a=int(input("Ingresa el primer número"))
    b=int(input("Ingresa el segundo número"))
    if amigos(a,b):
        print(a,"y",b,"son números amigos")
    else:
        print(a,"y",b,"no son números amigos")