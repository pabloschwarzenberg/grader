def buscarTodas(a, b):
    indices = []
    longitud_b = len(b)
    longitud_a = len(a)
    for i in range(longitud_a - longitud_b + 1):
        if a[i:i+longitud_b] == b:
            indices.append(str(i))
    return ' '.join(indices)
if __name__ == "__main__":
    a = input("Ingrese el string a: ")
    b = input("Ingrese el string b: ")
    resultado = buscarTodas(a, b)
    print("Resultado:", resultado)