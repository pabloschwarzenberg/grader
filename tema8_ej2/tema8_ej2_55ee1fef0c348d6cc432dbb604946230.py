def buscarTodas(a, b):
    index = 0
    indexA = []
    indexAString = ""
    while (index < len(a)):
        if (a[index] == b):
            indexA.append(index)
        index += 1
    for i in indexA:
        if (i == indexA[-1]):
            indexAString += str(i)
        else:
            indexAString += str(i) + " " 
    return indexAString

           