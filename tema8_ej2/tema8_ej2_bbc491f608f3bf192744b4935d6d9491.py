def buscarTodas(a,b):
    indices = []
    start = 0
    index = a.find(b, start)
    while index != -1:
        indices.append(str(index))
        start = index + 1
        index = a.find(b, start)
    return ' '.join(indices)

if __name__ == "__main__":
    a = input("Ingrese el string a: ")
    b = input("Ingrese el string b: ")
    resultado = buscarTodas(a, b)
    print("Apariciones encontradas en los índices:", resultado)