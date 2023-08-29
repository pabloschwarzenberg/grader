def buscarTodas(a, b):
    indices = []
    start = 0
    while True:
        pos = a.find(b, start)
        if pos == -1:
            break
        indices.append(str(pos))
        start = pos + len(b)
    return ' '.join(indices)

if __name__ == "__main__":
    a = input("Ingresa el string a: ")
    b = input("Ingresa el string b: ")
    resultado = buscarTodas(a, b)
    print("Los índices encontrados son:", resultado)

           