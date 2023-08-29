def buscarTodas(a,b):
    a=list(a)
    resultado=[]
    n=0
    for i in a:
        if i == b:
            resultado.append(str(n))
        n=n+1


    solucion = ' '.join(resultado)
    return solucion
    

