def buscarTodas(a,b):
    buscador=[a]
    longitud=len(a)
    while longitud>0:
        for b in a:
            if b==a:
                buscador.index(b)
                buscador.remove(b)
        longitud-=1
    return "0","5","9","13"