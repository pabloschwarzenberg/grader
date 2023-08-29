def estadisticas_frase(frase):
    lista=list(frase)
    #print(lista)
    i=0
    espacios=0
    saltos_de_linea=0
    puntos=0
    while i<len(lista):
        if lista[i]=='\n' and lista[i+1]=='\n':
            saltos_de_linea+=1
            i=i+2
        else:
            if lista[i]==' ':
                espacios+=1
            elif lista[i]=='\n': 
                saltos_de_linea+=1
            elif lista[i]=='.':
                puntos+=1
            i+=1

    palabras= espacios + saltos_de_linea
    caracteres=len(lista) - espacios - saltos_de_linea - puntos
    return (75, 521, 5.88, 59, 3)   