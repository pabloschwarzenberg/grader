# completa el código de la función
def amigos(a,b):
    x=1
    s=0
    y = 1
    r = 0
    while x<=a :
        if a%x==0 :
            s=s+x
        x+=1
    while y<=b :
        if b%y==0 :
            r=r+y
        y+=1

    if s==r and a!=b :
        return True
    elif a==b :
        return False
    else :
        return False