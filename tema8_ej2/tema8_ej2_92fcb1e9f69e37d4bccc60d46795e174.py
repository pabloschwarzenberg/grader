def buscarTodas(a, b):
    idx = 0
    idxA = []
    idxAStr = ""
    while idx < len(a):
        if a[idx] == b:
            idxA.append(idx)
        idx += 1
    for i in idxA:
        if i == idxA[-1]:
            idxAStr += str(i)
        else:
            idxAStr += str(i) + " " 
    return idxAStr