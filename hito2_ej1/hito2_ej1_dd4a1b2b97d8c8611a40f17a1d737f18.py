def secuencias(x1,y1):
    print (x1,y1)
    for n in x1:
        if not n in y1:
            i=x1.index(n)
            y1=y1.replace(y1[i],"_")
    print(y1)      