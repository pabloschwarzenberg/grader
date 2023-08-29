def suma_divisores(a):
    lista=[]
    for i in range(1,a):
        division=a/i
        if division %2 == 1:
            lista.append(i)
        if division %2 ==0:
            lista.append(i)
    suma = sum(lista)
    if suma == 7:
        return 7,False
    elif suma % 2 == 1:
        return suma,True
    elif suma % 2 == 0:
        return suma,False
    elif suma == 7:
        return 7,False