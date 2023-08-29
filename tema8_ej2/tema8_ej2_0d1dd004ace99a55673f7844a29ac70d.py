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
    texto_a = input("Ingrese el texto a buscar: ")
    texto_b = input("Ingrese el texto a encontrar: ")
    resultado = buscarTodas(texto_a, texto_b)
    print(resultado)
