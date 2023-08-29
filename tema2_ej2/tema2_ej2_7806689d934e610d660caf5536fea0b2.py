# completa el código de la función
def amigos(a,b):
    f=a
    h=b
    s=0
    c=0
    i=0
    while a>1:
        a=a-1
        if f%a==0:
            s=s+a
            if s==b:
                c=1
    while b>1:
        b=b-1
        if h%b==0:
            i=i+b
            if i==f:
               c=c+1
    if c==2:
        return True
    else:
        return False
            


if __name__=="__main__":
    a=int(input("Ingrese el primer numero: "))
    b=int(input("ingrese el segundo numero: "))
    print(amigos(a,b))
    
            
            

           