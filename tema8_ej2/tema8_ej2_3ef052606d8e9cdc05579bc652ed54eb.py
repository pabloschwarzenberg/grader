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
    resultado = buscarTodas(a, b)
    print(f"Índices encontrados: {resultado}")
