def rot13(palabra):
    alfabeto="abcdefghijklmnopqrstuvwxyz"
    lista=list(palabra)
    for i in range(len(lista)):
        alfalugar=alfabeto.find(palabra[i])
        if alfalugar+13<=25:
            lista[i]=alfabeto[alfalugar+13]
        else:
            lugar=(alfalugar+13)-26
            lista[i]=alfabeto[lugar]
    return "".join(lista)