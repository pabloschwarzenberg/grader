def numero_perfecto(a):
    d=a
    h=0
    while a>1:
        a=a-1
        if d%a==0:
            h=h+a
    if h==d:
        return True
    else:
        return False
if __name__=="__main__":
    j=0
    i=0
    a=int(input("Ingrese a: "))
    while i<a:
        if numero_perfecto(i)==True:
            j=j+i
        i=i+1
    print("La suma es: ",j)