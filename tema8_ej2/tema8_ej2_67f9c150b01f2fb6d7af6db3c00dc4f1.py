def buscarTodas(a, b):
    indices = []
    
    for i in range(len(a)):
        if a[i:i+len(b)] == b:
            indices.append(str(i))
    
    return ' '.join(indices)

if __name__ == "__main__":
    cadena_a = input("Ingrese el primer string: ")
    cadena_b = input("Ingrese el segundo string: ")
    
    resultado = buscarTodas(cadena_a, cadena_b)
    print("Resultado:", resultado)

           