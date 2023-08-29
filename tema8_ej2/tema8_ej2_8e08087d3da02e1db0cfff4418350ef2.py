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
    a = input("Ingrese una cadena: ")
    b = input("Ingrese la subcadena a buscar: ")
    resultado = buscarTodas(a, b)
    print("Índices de aparición:", resultado)

           