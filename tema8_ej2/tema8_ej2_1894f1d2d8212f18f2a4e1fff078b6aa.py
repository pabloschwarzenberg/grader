def buscarTodas(a,b):
    vari = 0
    variA = []
    varixAString = ""
    while (vari < len(a)):
        if (a[vari] == b):
            variA.append(vari)
        vari += 1
    for i in variA:
        if (i == variA[-1]):
            varixAString += str(i)
        else:
            varixAString += str(i) + " " 
    return varixAString