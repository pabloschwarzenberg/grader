

def buscarTodas(a,b):
    L=[]
    for x in range(len(a)):
        if a[x]==b:
            L.append(str(x))
    return " ".join(L)

    
           