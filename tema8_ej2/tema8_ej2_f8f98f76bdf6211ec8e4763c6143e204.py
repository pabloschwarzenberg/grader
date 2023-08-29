def buscarTodas(a, b):
    indices = []
    for i in range(len(a)):
        if a[i:i+len(b)] == b:
            indices.append(str(i))
    return " ".join(indices)

if __name__ == "__main__":
    a = input("Ingresa el string a: ")
    b = input("Ingresa el string b: ")
    indices = buscarTodas(a, b)
    print(indices)