def buscarTodas(a,b):
    lista = []
    for x in range(len(a)):
        if(a[x] == b):
            lista.append(x)
        pass
    return lista
text_str = str(buscarTodas("tres tristes tigres","t"))[1:-1]
text_str2 = text_str.replace(",","") 