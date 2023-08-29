def buscarTodas(a,b):
    L=list(a)
    l=len(L)
    l1=[]
    for i in range(l):
        if L[i]==b:
            l1.append(i)
    indices=""
    for i in range(len(l1)):
        if i!=len(l1)-1:
          indices+=str(l1[i])+" "
        else:
          indices+=str(l1[i])
    return indices  