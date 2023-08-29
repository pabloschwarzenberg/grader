# completa el código de la función
def amigos(a,b):
if a==b:
        return False
    for a in range(1,500):
        s=0
        for n in range(1,a):
            if a%n ==0:
                s=s+n
    for b in range(1,500):
        t=0
        for n in range(1,b):
            if a%n==0:
                t=t+n
                if s==b and t==a and a!=b:
                    print(a,b)
                    return False
                else:
                    return True
print(amigos(220,284))
           