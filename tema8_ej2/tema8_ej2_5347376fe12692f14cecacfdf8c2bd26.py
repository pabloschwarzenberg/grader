def buscarTodas(a,b):
index = []
lista = list(a)
for i in lista:
    if lista[i] == b:
        pos = lista.index()
    if pos not in index:
        index.append(pos)
return index

if __name__ == "__main__":
    pass
           