def amigos(a,b):
    m=a
    n=b
    p=0
    q=0
    r=0
    while a>1:
        a=a-1
        if m%a==0:
            p=p+a
            if p==b:
                q=1
    while b>1:
        b=b-1
        if n%b==0:
            r=r+b
            if r==b:
                q=q+1
    if q==2:
        return True
    if q!=2:
        return False
if __name__=="__main__":
    a=int(input("ingresa numero a verificar: "))
    b=int(input("ingresa el segundo numero: "))
    print(amigos(a,b))
           