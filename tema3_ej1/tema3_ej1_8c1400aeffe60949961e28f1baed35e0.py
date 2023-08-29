def suma_divisores(a):
    n=0
    for i in range(n+1,a):    
        if a==i:
            n=1
            break
        elif a%i!=0:
            pass
        elif a%i==0:
            n+=i
    while n!=1:
        return (n,False)
    else:
        return (n,True)

if __name__=="__main__":
    numero=int(input("ingrese un numero: "))
    resultado=suma_divisores(numero)
    print(resultado)
           