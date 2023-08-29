def numero_perfecto(a):
    estado=0
    suma=0
    for n in range(1,a):
        if a%n==0:
            m=n
            suma += m
    if suma==a:
        estado=True
    if not(suma==a):
        estado=False
            
    return estado


if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))