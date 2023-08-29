def numero_perfecto(a):
    divisores=[]
    for i in range(1,a):
        if a%i==0:
            divisores.append(i)
    suma=sum(divisores)
    if suma==a:
        return True
    elif suma!=a:
        return False
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           