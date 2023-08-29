def numero_perfecto(a):
    suma=0
    for i in range(1,a):
        if a%i==0:
            suma=suma+i
        else:
            pass
    if suma==a:
        return True
    elif suma!=a:
        return False

if __name__=="__main__":
    b=int(input())
    print(numero_perfecto(b))
           