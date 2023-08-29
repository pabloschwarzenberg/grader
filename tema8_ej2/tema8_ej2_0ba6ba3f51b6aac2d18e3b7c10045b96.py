def buscarTodas(a,b):
    lista_a=list(a)
    posiciones=[]
    for p in lista_a:
        if p==b:
            posicion=lista_a.index(p)
            lista_a[posicion]="-"
            posiciones.append(str(posicion))
    lugar=" ".join(posiciones)
    return lugar
    pass

if __name__ == "__main__":
    pass
           