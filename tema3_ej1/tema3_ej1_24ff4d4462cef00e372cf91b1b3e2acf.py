def suma_divisores(a):
    lista=[]
    ne= 0
    for j in range(1,a):
        if a%j == 0:
            ne =ne + j
            lista.append(j)
    
    if len(lista)==1:
        j= True
    else:
        j= False
    
    return ne,j