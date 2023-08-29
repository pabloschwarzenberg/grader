def buscarTodas(a, b):
    indices = []
    indice = a.find(b)
    while indice != -1:
        indices.append(str(indice))
        indice = a.find(b, indice + 1)
    return " ".join(indices)

if __name__ == "__main__":
    a = input("Ingrese el string a: ")
    b = input("Ingrese el string b: ")
    resultado = buscarTodas(a, b)
    print("Secuencia de índices:", resultado)
