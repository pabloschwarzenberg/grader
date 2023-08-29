def numero_perfecto(a):
    t=a//2
    suma=0
    for i in range(1,t+1):
        k=a%i
        if k==0:
            suma+=i
        else:
            continue
    if suma==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           