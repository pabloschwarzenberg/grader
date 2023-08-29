# completa el código de la función
def amigos(a,b):
    r1=0
    for i in range(1,a):
        if a%i==0:
            r1=r1+i
    r2=0
    for i in range(1,b):
        if b%i==0:
            r2=r2+i
    if r1==b and r2==a:
        return True
    else:
        return False

#amigos(eval(input("Ingrese A: ")),eval(input("Ingrese B: ")))
