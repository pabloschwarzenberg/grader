def numero_perfecto(a):
    n=0
    for i in range(n+1,a):    
        if a==i:
            n=1
            break
        elif a%i!=0:
            pass
        elif a%i==0:
            n+=i
    while n==a:
        return True
    else:
        return False

if __name__=="__main__":
    numero=int(input("ingrese un numero: "))
    resultado=numero_perfecto(numero)
    print(resultado)
