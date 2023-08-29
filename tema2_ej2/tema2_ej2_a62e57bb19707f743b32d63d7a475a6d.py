# completa el código de la función
#numeros amigos

def amigo(a,b):
    m = 0
    s = 0
    d = 0
    f = 0
    
    
    
    
    while m < a-1:
        m += 1
        if a%m==0:
            s += m
    while d < b-1:
        d += 1
        if b%d==0:
            f += d
    if s==f:
        print("True")
    else:
        print("False")


amigo(12,11)

