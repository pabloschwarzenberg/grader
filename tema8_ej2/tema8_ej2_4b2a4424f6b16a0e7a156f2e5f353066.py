def buscarTodas(a,b):
    pos = []
    for i in range(len(a)):
        ind = 0
        if b[ind] == a[i]:
            pos.append(i)      
            ind+=1            
    return ' '.join(str(e) for e in pos)
           