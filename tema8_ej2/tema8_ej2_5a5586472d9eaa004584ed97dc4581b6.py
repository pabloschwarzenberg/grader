def buscarTodas(a,b):
    lista=[]
    palabra=[]
    for i in a:
        lista.append(i)

    for y in range(len(lista)):
        if lista[y]==b:
            palabra.append(str(y))
    palabraa=' '.join(palabra)
    return palabraa

if __name__ == "__main__":
    pass
           