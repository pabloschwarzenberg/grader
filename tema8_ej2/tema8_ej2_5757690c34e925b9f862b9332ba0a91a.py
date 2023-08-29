def buscarTodas(a, b):
    indices = []
    inicio = 0
    
    while inicio < len(a):
        indice = a.find(b, inicio)
        
        if indice != -1:
            indices.append(str(indice))
            inicio = indice + 1
        else:
            break
    
    return ' '.join(indices)

if __name__ == "__main__":
    a = input("Ingrese el string a: ")
    b = input("Ingrese el string b: ")
    resultado = buscarTodas(a, b)
    print("Secuencia de índices: ", resultado)

           