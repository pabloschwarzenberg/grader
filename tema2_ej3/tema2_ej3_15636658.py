def numero_perfecto(a):
    k=a
    suma=0
    for i in range (a-1):
        if a==1:
            suma=1
        elif a%k==0:
            suma+=a//k
        k=k-1
    if suma==a and a!=1:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    suma=0
    for i in range (a):
        if numero_perfecto(i)==True:
            suma=suma+i
    print(suma)