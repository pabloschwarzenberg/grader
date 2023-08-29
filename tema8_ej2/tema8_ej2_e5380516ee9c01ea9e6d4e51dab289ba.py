def buscarTodas(a, b):
    indices = []
    longitud_b = len(b)
    
    for i in range(len(a)):
        if a[i:i+longitud_b] == b:
            indices.append(str(i))
    
    return " ".join(indices)

if __name__ == "__main__":
    a = input("Ingresa el string a: ")
    b = input("Ingresa el string b: ")
    resultado = buscarTodas(a, b)
    print("Los índices encontrados son:", resultado)
