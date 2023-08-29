# completa el código de la función
def amigos(a,b):
        a=int(a)
        b=int(b)
        c=range(1,a-1)
        d=range(1,b-1)
        e=0
        f=0
        for i in c:
                if (a%i==0):
                        e+=i
        for j in d:
                if(b%j==0):
                        f+=j
        if (a==f) and (b==e):
                return True
        else:
                return False
           