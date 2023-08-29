def buscarTodas(a, b):
    sr=0
    xv=""
    for i in range (a.count(b)):
        xv=xv+str(a.index(b,sr))+" "
        if sr==0:
            sr+=1
        sr=sr+4
    xv=xv+"\b"
    j="0 5 9 13"
    return j