def buscarTodas(a, b):
    contador = 0
    encontrado = ""

    for x in a:
        if x == b:
            encontrado = encontrado+ " " +str(contador)
        contador = contador + 1

    strFinal = encontrado.lstrip()

    return strFinal
    pass


if __name__ == "__main__":
    var = buscarTodas("tres tristes tigres","t")
    print(var)
    pass
