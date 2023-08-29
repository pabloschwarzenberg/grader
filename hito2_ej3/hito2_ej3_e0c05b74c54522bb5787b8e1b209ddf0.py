def substring(string,n):
    contador_1=0
    contador_2=n
    lista_1=[]
    lista_2=[]
    while contador_2<=len(string):
        lista_1.append(string[contador_1:contador_2])
        contador_1+=1
        contador_2+=1
    for i in range(len(lista_1)):
        if lista_1[i] not in (lista_1[:i]+lista_1[i+1:]):
            lista_2.append(lista_1[i])
    if len(lista_2)>0:
        for i in range(len(lista_2)):
            lista_2[i] = lista_2[i].lower()
    else:
        lista_2.append('ninguna')
    return lista_2

string = str(input())
n=int(input())
print(substring(string,n))

     