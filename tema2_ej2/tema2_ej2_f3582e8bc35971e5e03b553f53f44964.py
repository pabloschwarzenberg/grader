# completa el código de la función
def amigos(a,b):
    if a==b:
        return False
    x=a+1
    y=b+1
    divisor=2
    if a==1 or a==0 or b==1 or b==0:
        return False
    while divisor<a:
        if a%divisor==0:
            x+=divisor
        divisor+=1
    divisor=2
    while divisor<b:
        if b%divisor==0:
            y+=divisor
        divisor+=1
    if x==y:
        return True
    else:
        return False
print(amigos(3,8))

           