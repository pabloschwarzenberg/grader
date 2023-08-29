def buscarTodas(a, b):
    indices = []
    start = 0
    while True:
        index = a.find(b, start)
        if index == -1:
            break
        indices.append(str(index))
        start = index + 1
    return ' '.join(indices)

if __name__ == "__main__":
    a = input("Ingrese el string a: ")
    b = input("Ingrese el string b: ")
    indices_encontrados = buscarTodas(a, b)
    print("Secuencia de índices encontrados:", indices_encontrados)
