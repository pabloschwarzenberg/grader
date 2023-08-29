# completa el código de la función
# completa el código de la función
def amigos(a,b):
    c=0
    d=0
    for i in range(1,a):
        if a%i==0:
            c+=i
    for i in range(1,b):
        if b%i==0:
            d+=i
    if d==a and c==b:
        return True 
    else:
        return False