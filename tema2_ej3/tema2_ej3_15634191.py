def numero_perfecto(a):
    divA=0
    for i in range(1,a):
        if a%i==0:
            divA+=i
    if divA==a:
        return True
    else:
        return False

if __name__=="__main__":
    suma=0
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
    n=int(input("Ingrese numero n: "))
    for i in range(1,n):
        if numero_perfecto(i)==True:
            suma+=i
    print(suma)
           