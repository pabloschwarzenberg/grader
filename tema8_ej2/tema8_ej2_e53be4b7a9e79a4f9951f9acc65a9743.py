def buscarTodas(a,b):
    c = ""
    x = -1
    for i in a:
        x += 1
        if i == b:
            c = c+str(x)+str(" ")
    return c.rstrip()