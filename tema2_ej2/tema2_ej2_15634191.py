# completa el código de la función
def amigos(a,b):   
    divA=0
    divB=0
    for i in range(1,a):
        if a%i==0:
            divA+=i
    for i in range(1,b):
        if b%i==0:
            divB+=i
    if divA==b and divB==a:
        return True
    else:
        return False