def buscarTodas(a, b):
    indices = []
    inicio = 0
    while inicio < len(a):
        indice = a.find(b, inicio)
        if indice == -1:
            break
        indices.append(str(indice))
        inicio = indice + 1
    return ' '.join(indices)

if __name__ == "__main__":
    texto = input("Ingrese el texto: ")
    patron = input("Ingrese el patrón a buscar: ")
    resultados = buscarTodas(texto, patron)
    print("Apariciones encontradas en los índices:", resultados)
