# completa el código de la funcióndef amigos(a,b):
def amigos(a,b):
    suma1=0
    suma2=0
    for i in range(1,a+1):
        if a%i==0:
            suma1+=i
    for i in range(1,b+1):
        if b%i==0:
            suma2+=i
    if suma1==suma2 and a!=b:
        return True
    if suma1!=suma2 or a==b:
        return False