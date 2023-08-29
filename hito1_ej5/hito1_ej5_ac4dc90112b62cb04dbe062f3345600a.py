rut=input("Ingrese su rut, sin digito verificador: ")
lista=[]
a = len(rut)
if a==7:
    for i in range(len(rut)):
        lista.append(rut[i])
    lista.reverse()
    a=2
    lista2=[]
    print(len(lista))
    for j in range(int(len(lista))):
        if a>=2 and a<=7:
            b = int(lista[j]) * a
            a = a + 1
            lista2.append(b)
        elif a>7:
            a=2
            b = int(lista[j]) * a
            a = a + 1
            lista2.append(b)
    print(lista2)
    lista2=sum(lista2)
    print(lista2)
    r = lista2%11
    dv= 11-r
    if (dv == 10):
        print("dv=k")
    elif (dv==11):
        print("dv=0")
    else:
        print("dv=",dv)
elif a==8:
    for i in range(len(rut)):
        lista.append(rut[i])
    lista.reverse()
    a=2
    lista2=[]
    for j in range(int(len(lista))):
        if a>=2 and a<=7:
            b = int(lista[j]) * a
            a = a + 1
            lista2.append(b)
        elif a==8:
            a=2
            b = int(lista[j]) * a
            a = a + 1
            lista2.append(b)
    lista2=sum(lista2)
    print(lista2)
    r= lista2%11
    dv=11-r
    if (dv == 10):
        print("dv=k")
    elif (dv==11):
        print("dv=0")
    else:
        print("dv=",dv)