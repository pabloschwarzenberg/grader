def buscarTodas(a, b):
    indices = []
    pos = a.find(b)
    while pos != -1:
        indices.append(str(pos))
        pos = a.find(b, pos + 1)
    return " ".join(indices)

if __name__ == "__main__":
    a = input("Ingrese el string a: ")
    b = input("Ingrese el string b: ")
    resultado = buscarTodas(a, b)
    print("Las apariciones de", b, "en", a, "son:", resultado)
