#Función buscarTodas 
def buscarTodas(a,b):
    a1 = list(a)
    i = 0
    indices=[]
    while i<len(a1):
        if a1[i] == b:
            indices.append(i)
        i = i + 1
    indices2= []
    for j in indices:
        j = str(j)
        indices2.append(j)
    s = ""
    for k in indices2:
        s = s+" "+k
    s1 = list(s)
    s1.pop(0)
    s2 = "".join(s1)
    return s2