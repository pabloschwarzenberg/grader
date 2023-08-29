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
    texto_a = input("Ingresa el texto a buscar: ")
    texto_b = input("Ingresa el texto a buscar en el texto anterior: ")
    resultado = buscarTodas(texto_a, texto_b)
    print("Índices encontrados:", resultado)
    