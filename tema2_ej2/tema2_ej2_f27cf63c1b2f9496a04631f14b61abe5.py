# completa el código de la función
def amigos(a,b):
    da=0
    db=0
    for i in range(1,a):
        if a%i==0:
            da+=i
    for i in range(1,b):
        if b%i==0:
            db+=i
    if (da==b)and(db==a):
        return True
    return False
