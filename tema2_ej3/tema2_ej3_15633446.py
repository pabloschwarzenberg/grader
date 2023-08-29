def numero_perfecto(a):
    divisores=0
    for i in range(1,a):
        r=a%i
        if(r==0):
            divisores += i
    if(divisores==a):
        u=True
    else:
        u=False
    return(u)

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           