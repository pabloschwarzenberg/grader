def numero_perfecto(a):
    suma=0
    for m in range(1,a):
        if a%m==0:
            suma=suma+m
    if suma==a:
        return (True)
    else:
        return (False)

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
