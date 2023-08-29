def buscarTodas(a,b):
    cont = 0
    lista = list(a)
    acumul = ""
    for letras in a:
         if lista [cont] == b:
            acumul += str(cont) + " "
         cont += 1
    o = list(acumul)
    listaA = len(o)
    del o [listaA - 1] 
    o = "".join(o)
    return(o)
print(buscarTodas("tres tristes tigres","t"))