def buscarTodas(a,b):
    a=list(a)
    indices=[]
    aparaciones=0
    largo_palabra=len(a)
    conta_min=0
    while conta_min < largo_palabra:
        if b == a[conta_min]:
            indices.append(conta_min)
            aparaciones+=1
        conta_min=conta_min+1
    index_f=' '.join(str(e) for e in indices)
    return index_f