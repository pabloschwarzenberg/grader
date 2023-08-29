def buscarTodas(a, b):
    indices = []
    inicio = 0
    while True:
        indice = a.find(b, inicio)
        if indice == -1:
            break
        indices.append(str(indice))
        inicio = indice + 1
    return ' '.join(indices)


if __name__ == "__main__":
    texto = 'tres tristes tigres'
    patron = 't'
    resultado = buscarTodas(texto, patron)
    print(resultado)
