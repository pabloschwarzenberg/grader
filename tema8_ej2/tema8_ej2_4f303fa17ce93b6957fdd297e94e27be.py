def buscarTodas(a,b):
    res =""
    pos = 0
    for i in a:
        if i == b:
            if pos == 0:
                res+=str(pos)
            else:
                res+=" "+str(pos)
        pos +=1
    return res