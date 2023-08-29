def buscarTodas(a,b):
    lista = ""
    pos_inicial = -1
    try:
        while True:
            pos_inicial = a.index(b, pos_inicial+1)
            lista += str(pos_inicial)
            lista +=(" ")
    except ValueError:
        
        return lista[:-1]

           