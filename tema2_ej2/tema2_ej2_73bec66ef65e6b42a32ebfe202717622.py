# completa el código de la función
def amigos(a,b):
    lista_a=[]
    a1=a-1
    while a1>0:
        if a%a1==0:
            lista_a.append(a1)
        a1=a1-1
    lista_b=[]
    b1=b-1
    while b1>0:
        if b1%b==0:
            lista_b.append(b1)
        b1=b1-1
    suma_a=0
    for i in lista_a:
        suma_a=suma_a+i
    suma_b=0
    for j in lista_b:
        suma_b=suma_b+j
    if suma_a==suma_b:
        return True
    elif suma_a!=suma_b:
        return False