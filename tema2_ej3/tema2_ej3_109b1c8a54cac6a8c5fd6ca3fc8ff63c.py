def numero_perfecto(a):
    a=int(a)
    x=0
    b=1
    while b<a:
        if a%b==0:
            x=x+b
        b=b+1
    if x==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           