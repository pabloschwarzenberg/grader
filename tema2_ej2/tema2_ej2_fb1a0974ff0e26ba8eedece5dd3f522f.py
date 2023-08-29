# completa el código de la función
def amigos(a,b):
#suma de a
    s=0
    n=1
    ss=0
    nn=1
    while n<a:
        if a%n==0:
            s=s+n
            n=n+1
        else:
            n=n+1
    #print(s)

#suma de b
    while nn<b:
        if b%nn==0:
            ss=ss+nn
            nn=nn+1
        else:
            nn=nn+1

    if s==b and ss==a:
        return True

    else:
        return False
     
           