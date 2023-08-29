def buscarTodas(a,b):
index = []
lista = list(a)
for i in lista:
    if i == b:
        pos = lista.index()
    if pos not in index:
        index.append(pos)
return index