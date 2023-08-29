# completa el código de la función
def amigos(a,b):
    B=0
    for i in range(1,a):
        if a%i==0:
            B+=i
    if B==b:
        return True
    return False           