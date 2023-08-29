def numero_perfecto(a):
    s=0
    d=1
    for d in range(1,a):
        if(a%d==0):
            s=s+d
    if(s==a):
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))


if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))