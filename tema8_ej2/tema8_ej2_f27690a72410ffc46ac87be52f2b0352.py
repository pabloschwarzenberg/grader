def buscarTodas(a, b):
    resultado = ""
    inicio = 0
    
    while True:
        indice = a.find(b, inicio)
        
        if indice == -1:
            break
        
        resultado += str(indice) + " "
        inicio = indice + 1
    
    return resultado.strip()

if __name__ == "__main__":
    cadena_a = input("Ingresa la cadena a: ")
    cadena_b = input("Ingresa la cadena b: ")
    indices = buscarTodas(cadena_a, cadena_b)
    print("Secuencia de índices: ", indices)
