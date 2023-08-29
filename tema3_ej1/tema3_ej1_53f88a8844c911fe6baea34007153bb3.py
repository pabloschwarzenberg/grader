def suma_divisores(a):
    lista_de_divisores=[]
    suma=0
    for i in range(1,a):
        if a%i==0:
            lista_de_divisores.append(i)
    for x in lista_de_divisores:
        suma+=x

    if suma==1:
        return suma,True
    else:
        return suma,False


if __name__=="__main__":
    a=int(input("Ingrese un número: "))
    print(suma_divisores(a))