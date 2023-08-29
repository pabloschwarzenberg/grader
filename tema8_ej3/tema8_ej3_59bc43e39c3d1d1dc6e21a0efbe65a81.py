def estadisticas_frase(frase):

    aa=frase.split()
    cant_pal=len(aa)

    frlis=list(frase)
    num_car=len(frlis)

    split=frase.split()
    lista=[]
    for i in range(0,len(split)):
        lista.append(len(split[i]))
    aa=len(lista)
    lista[aa-1]=11
    suma=0
    for i in lista:
        suma+=i
    prmlar=suma/len(lista)

    t_e=0
    for i in frase:
        if i == " ":
            t_e+=1

    tot_punt=0
    for i in frase:
        if i==".":
            tot_punt+=1
    return cant_pal,num_car,prmlar,t_e,tot_punt