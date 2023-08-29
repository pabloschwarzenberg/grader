def numero_perfecto(a):
    lista=[]
    suma=0
    for i in range(1,a):
        if a%i==0:
            lista.append(i)
    for e in lista:
        suma+=e
    if suma==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           