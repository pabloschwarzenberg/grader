def buscarTodas(a, b):
    lista = []
    lista_1 = []
    cont = 0

    for i in a:
        if i == b:
            lista.append(cont)
        cont += 1
    for i in lista:
        lista_1.append(str(i))
    return " ".join(lista_1)


if __name__ == "__main__":
    a = input("Inserte frase cualquiera:")
    b = input("Inserte letra a buscar en la frase anterior:")
    r= buscarTodas(a, b)
    print(r)