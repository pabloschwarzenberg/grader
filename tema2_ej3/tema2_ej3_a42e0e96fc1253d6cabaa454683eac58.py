def numero_perfecto(a):
    suma=0
    
    for i in range(1,a):
        f=a%i
        if f==0:
            suma=suma+i
    valido=False
    if suma==a:
        valido=True
        
    return valido
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           