def buscarTodas(a,b):
    i = 0
    codigo = ""
    while i < len(a):
        if a[i:i + len(b)]==b:
            codigo +=  str(i) + " " 
        i += 1
    return codigo