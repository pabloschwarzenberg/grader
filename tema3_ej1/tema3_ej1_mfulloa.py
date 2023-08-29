def suma_divisores(a):
    lista_a=[]
    contador=1
    suma_a=0
    while contador<a:
        if a%contador==0:
            lista_a.append(contador)
            contador+=1
        else:
            contador+=1
    for i in lista_a:
        suma_a+=i
    if suma_a==1:
        return suma_a,True
    else:
        return suma_a,False
if __name__=="__main__":
    a=int(input("Ingrese el número: "))
    print(suma_divisores(a))
