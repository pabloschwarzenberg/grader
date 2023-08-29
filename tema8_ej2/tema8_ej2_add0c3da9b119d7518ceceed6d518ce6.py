def buscarTodas(a,b):
    z=[i for i, x in enumerate(a) if x==b]
    v = ''.join(str(v) for v in z)
    y = str(v)
    return y
          