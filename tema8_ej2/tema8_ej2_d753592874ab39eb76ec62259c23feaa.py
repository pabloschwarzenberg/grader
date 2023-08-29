def buscarTodas(palabra_larga,palabra):
    lista=[]
    i=0
    while i in range(len(palabra_larga)):
        for j in palabra:
            if palabra_larga[i]==j:
                lista.append(i)
                lista.append(" ")
        i+=1
        lista2=[]
        for q in lista:
            if type(q)==str():
                lista2.append(q)
            else:
                a=str(q)
                lista2.append(a)
    lista2.pop(len(lista2)-1)
    p="".join(lista2)
    return p

if __name__ == "__main__":
    pass
           