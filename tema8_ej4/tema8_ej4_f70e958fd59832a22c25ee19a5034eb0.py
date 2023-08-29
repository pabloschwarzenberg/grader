def  rot13 (palabra):
    p= ""
    l=list(map(chr, range(97, 110)))
    l1=list(map(chr, range(110, 123)))
    for j in range (0, len(palabra)):
        for i in range (0,13):
            if(palabra[j]==l[i]):
                p=p+l1[i]
            if(palabra[j]==l1[i]):
                p=p+l[i]
    return(p)