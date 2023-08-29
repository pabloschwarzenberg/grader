def amigos(a,b):
    lista_a=[]
    lista_b=[]
    contadora=1
    contadorb=1
    suma_a=0
    suma_b=0
    while contadora<a:
        if a%contadora==0:
            lista_a.append(contadora)
            contadora+=1
        else:
            contadora+=1
    while contadorb<b:
        if b%contadorb==0:
            lista_b.append(contadorb)
            contadorb+=1
        else:
            contadorb+=1
    for i in lista_a:
        suma_a=suma_a+i
    for j in lista_b:
        suma_b=suma_b+j
    if suma_a==b and suma_b==a:
        return True
    else:
        return False
if __name__=="__main__":
    a=int(input("Ingrese primer número: "))
    b=int(input("Ingrese segundo número: "))
    print(amigos(a,b))
