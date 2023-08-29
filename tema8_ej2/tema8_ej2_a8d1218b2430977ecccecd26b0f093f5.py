def buscarTodas(a, b):
    indices = []
    start = 0
    while True:
        index = a.find(b, start)
        if index == -1:
            break
        indices.append(str(index))
        start = index + 1
    return " ".join(indices)

if __name__ == "__main__":
    texto = input("Ingrese el texto: ")
    buscar = input("Ingrese el string a buscar: ")
    resultado = buscarTodas(texto, buscar)
    print(resultado)
