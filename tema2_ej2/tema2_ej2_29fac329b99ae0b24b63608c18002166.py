# completa el código de la función
def amigos(a,b):
    s1=0
    s2=0
    for i in range(2,a):
        if(a%i==0):
            s1=s1+i
    for j in range(2,b):
        if(b%j==0):
            s2=s2+j

    if(s1==b):
        return True
    elif(s2==a):
        return True
    else:
        return False