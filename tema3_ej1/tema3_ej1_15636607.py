def suma_divisores(a):
    r=0
    i=1
    if a==1:
        r=0
    else:
        while i<a:
            if a%i==0:
                r=r+i
                i=i+1
            else:
                i=i+1
    if r==1:
        p=True
    else:
        p=False
    return (r,p)
if __name__=="__main__":
    a=int(input("ingrese a:"))
    print(suma_divisores(a))
