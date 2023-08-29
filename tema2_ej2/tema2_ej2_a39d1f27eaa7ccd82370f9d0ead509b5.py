def divisores(numero):
    cont=1
    lista=[]
    while cont<numero:

        calculo=numero%cont

        if calculo==0:
            lista.append(cont)
        cont+=1

    return lista
def amigos(a,b):
    lista1=divisores(a)
    lista2=divisores(b)

    lista1=sum(lista1)
    lista2=sum(lista2)
    if lista1==b and lista2==a:
        return True

    else:
        return False
