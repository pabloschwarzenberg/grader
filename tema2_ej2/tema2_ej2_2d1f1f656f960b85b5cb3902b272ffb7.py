# completa el código de la función
def amigos(a,b):
    W=1
    X=1
    Y=0
    Z=0
    while W < a:
        if a%W==0:
            Y+=W
            print("divisor de %d es : %d" % (a,W),"la suma de divisores de %d es: %d" %(a, Y))
        W+=1
    while X < b:
        if b%X==0:
            Z+=X
            print("divisor de %d es: %d" % (b, X), "la suma de divisores de %d es: %d" %(b, Z))
        X+=1
    if Y==b and Z==a:
        return True
    else:
        return True
try:
    inc_1=int(input("numero 1°:"))
    inc_2=int(input("numero 2°:"))
    print(amigos(inc_1, inc_2))
except:
    print("por favoe ingrese un numero")