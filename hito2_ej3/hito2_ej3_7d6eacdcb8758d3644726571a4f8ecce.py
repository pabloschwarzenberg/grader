lista = []
def buscarTodas(a,b):
    i = 0
    while i < len(a):
        a.lower()
        b.lower()
        i = a.find(b, i)
        if i == -1:
            break
        j = str(i)
        lista.append(j)
        i += 1
        k = " ".join(lista)
    return (k)

if __name__ == "__main__":
    listongo = []
    string = input("Ingrese secuencia:" )
    string = string.lower()
    n = int(input("Ingrese rango: "))
    for i in range(len(string)):
        lista = []
        j = i
        k = n+i
        x = string[j:k]
        c = buscarTodas(string,x)
        if len(lista) == 1 and len(x) == n:
            listongo.append(x)
    if len(listongo) > 0:
        print(listongo)
    elif len(listongo) == 0:
        listita ='ninguna'
        print(listita)