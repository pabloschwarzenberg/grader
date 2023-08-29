def buscarTodas(a,b):
    a=list(a)
    contador=a.count(b,)
    posiciones=[""]
    while contador>0:
        a = list(a)
        pos=a.index(b)
        posiciones.append(str(pos))
        posiciones.append(" ")
        a[pos]="_"
        contador-=1
    posiciones.pop()
    n="".join(posiciones)
    return n

if __name__ == "__main__":
    pass
           