def buscarTodas(a, b):
    indices = []
    for i in range(len(a)):
        if a[i:i+len(b)] == b:
            indices.append(str(i))
    return ' '.join(indices)

if __name__ == "__main__":
    a = input("Ingrese el string a: ")
    b = input("Ingrese el string b: ")
    resultado = buscarTodas(a, b)
    print("Índices encontrados:", resultado)
