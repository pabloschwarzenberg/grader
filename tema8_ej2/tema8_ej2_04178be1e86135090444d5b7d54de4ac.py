def buscarTodas(a,b):
    dem = []
    for x in range(len(a)):
        if b == a[x]:
            dem.append(str(x)) #Agregar a la lista vacia
    return " ".join(dem)