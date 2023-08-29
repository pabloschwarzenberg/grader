# completa el código de la función
def amigos(a,b):
    c=0
    for i in range(1,a):
        if a%i==0:
            c+=i
    if c==b:
        return True
    else:
        return False
           