def buscarTodas(a, b):
    indices = []

    i = 0
    while i < len(a):
        if a[i:i+len(b)] == b:
            indices.append(str(i))
            i += len(b)
        else:
            i += 1

    return ' '.join(indices)

if __name__ == "__main__":
    a = input("Ingresa el string a: ")
    b = input("Ingresa el string b: ")
    resultado = buscarTodas(a, b)
    print("Secuencia de índices:")
    print(resultado)
    
           