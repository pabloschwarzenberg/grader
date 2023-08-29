def buscarTodas(a, b):
    indices = []
    length_b = len(b)
    
    for i in range(len(a) - length_b + 1):
        if a[i:i+length_b] == b:
            indices.append(str(i))
    
    return ' '.join(indices)

if __name__ == "__main__":
    a = input("Ingresa el string a: ")
    b = input("Ingresa el string b: ")
    resultado = buscarTodas(a, b)
    print("Resultado:", resultado)
