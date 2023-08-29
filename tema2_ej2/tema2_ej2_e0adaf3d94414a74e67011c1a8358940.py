# completa el código de la función
def amigos(a,b):
    for a in range(a,b):
        s=0
        for n in range(1,a):
            if a%n==0:
                s=s+n
            elif s == b:
              return True
    return False
    
