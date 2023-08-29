# completa el código de la función
a=1
b=2
def amigos(a,b):
    la=0
    for i in range(1,a) :
        if a%i==0:
            la=la+i
    lb=0
    for j in range(1,b) :
        if b%j==0:
            lb=lb+j
    print(la)
    print(lb)
    if lb==a and la==b:
        return True
    else:
        return False
    
resultado=amigos(a,b)
print(resultado)