def numero_perfecto(a):
    i=0
    suma=0
    perfecto=False
    for i in range(a-1):
        if a%(i+1)==0:
            suma=suma+1+i
    print(suma)
    if suma==a:
        perfecto=True
    return perfecto

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           
