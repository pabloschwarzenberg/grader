def buscarTodas(a,b):
    almacenamiento = []
    for i in range(len(a)):
        if (b == a[i]):
            almacenamiento.append(i)
    vez = str(almacenamiento)
    tal = almacenamiento[-1]
    lol = vez.replace(",", "")
    lol = lol.replace("[","")
    lol = lol.replace("]","")
        
    return lol