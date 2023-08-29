def numero_perfecto(a):
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
        suma_a=suma_a+i
    if suma_a==a:
        return True
    else:
        return False
if __name__=="__main__":
    a=int(input("Ingrese número: "))
    print(numero_perfecto(a))
