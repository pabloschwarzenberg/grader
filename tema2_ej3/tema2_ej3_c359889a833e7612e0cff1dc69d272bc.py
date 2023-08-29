def numero_perfecto(a):
    suma=0
    for i in range(1,a):
        rest=a%i
        if rest==0:
            suma=suma+i
    if suma==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           