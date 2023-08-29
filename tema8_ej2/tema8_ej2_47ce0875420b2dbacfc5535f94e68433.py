def buscarTodas(a,b):
    a=list(a)
    long_a=len(a)
    veces=a.count(b)
    posicion=0
    if veces>0:
        for i in range(0,long_a):
            posicion=posicion+" "+posicion
            posicion=a.index(b,a[posicion])
    return posicion
    pass

if __name__ == "__main__":
    pass
