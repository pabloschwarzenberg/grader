def buscarTodas(b,a):
    z=[i for i, x in enumerate(b) if x==a]
    v = ' '.join(str(v) for v in z)
    y = str(v) 
    return y
