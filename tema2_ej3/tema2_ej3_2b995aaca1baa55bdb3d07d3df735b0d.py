def numero_perfecto(a):
    suma=0
    a=int(a)
    for i in range(1,a-1):
        if a%i==0:
            suma+=i
    if suma==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           