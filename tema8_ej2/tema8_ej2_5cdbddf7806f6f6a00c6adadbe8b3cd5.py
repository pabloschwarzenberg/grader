def buscarTodas(a, b):
    indices = []
    index = 0
    while index < len(a):
        if a[index:index+len(b)] == b:
            indices.append(str(index))
            index += len(b)
        else:
            index += 1
    return ' '.join(indices)

if __name__ == "__main__":
    a = input("Ingrese el string a: ")
    b = input("Ingrese el string b: ")
    resultado = buscarTodas(a, b)
    print(resultado)
