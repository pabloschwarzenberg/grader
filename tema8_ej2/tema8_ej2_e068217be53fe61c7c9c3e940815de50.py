def buscarTodas(a,b):
    lista_a=list(a)
    lista=[]
    
    resultado=[i for i, n in enumerate(lista_a) if n == b]
    for i in resultado:
        lista.append(i)
    intento = ' '.join(str(e) for e in lista)
    return intento