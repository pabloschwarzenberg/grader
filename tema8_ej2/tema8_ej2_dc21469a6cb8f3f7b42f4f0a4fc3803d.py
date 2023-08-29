def buscarTodas(a,b):
    pass
if __name__ == "__main__":
    pass
def buscarTodas(a, b):
    indices = []
    pos = -1
    while True:
        pos = a.find(b, pos + 1)
        if pos == -1:
            break
        indices.append(str(pos))
    return ' '.join(indices)
if __name__ == "__main__":
    a = input("Ingrese el string a: ")
    b = input("Ingrese el string b: ")
    resultado = buscarTodas(a, b)
    print("Secuencia de índices:", resultado)           