def numero_perfecto(a):
    m=a
    b=0
    p=0
    q=0
    while a>1:
        a=a-1
        if m%a==0:
            p=p+a
            if p==b:
                q+=1
        if m%a!=0:
            p=p+a
            if p==b:
                q+=1
    if q==2:
        return True
    if q!=2:
        return False
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))

           