def buscarTodas(a,b):
    lista = []
    for i in range(0, len(a)):
        if a[i] == b:
            i = str(i)
            lista.append(i)
    franco=" ".join(lista)
    return franco

#x=input("Ingrese mierda: ")
#y = input("Inegrese la letra que quiere buscar en l a mierda: ")
#w = buscarTodas(x,y)
#print(w)
