def buscarTodas(a, b):
    palabra = []
    palabra1 = ""
    palabra2 = ""
    c=0
    for indice in a:
        if indice == b:
            palabra.append(c)

        c+=1


    for i in palabra:
        palabra1 = palabra1 + str(i) + " "
    for i in range(len(palabra1)-1):
        palabra2 += palabra1[i]
    return palabra2

