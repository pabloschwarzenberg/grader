def buscarTodas(a, b):
    indices = []
    indice = -1
    
    while True:
        indice = a.find(b, indice + 1)
        if indice == -1:
            break
        indices.append(str(indice))
    
    return ' '.join(indices)

if __name__ == "__main__":
    a = input("Ingrese el string a: ")
    b = input("Ingrese el string b: ")
    
    resultado = buscarTodas(a, b)
    print("Apariciones de", b, "en", a + ":", resultado)
