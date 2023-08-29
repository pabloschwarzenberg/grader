def buscarTodas(a,b):
    a = list(a)
    g = ""
    j = 0
    for d,c in enumerate(a):
        if c==b:
            g+= str(d)
            j+=1
            if j != (a.count(b)):
                g+=" "
    a = g
    return a

if __name__ == "__main__":
    pass
           