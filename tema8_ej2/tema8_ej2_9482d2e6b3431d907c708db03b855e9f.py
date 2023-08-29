def buscarTodas(a, b):
    indices = []
    inicio = 0
    while inicio < len(a):
        indice = a.find(b, inicio)
        if indice == -1:
            break
        indices.append(str(indice))
        inicio = indice + 1
    return ' '.join(indices)

if __name__ == "__main__":
    cadena = input("Ingrese una cadena: ")
    subcadena = input("Ingrese una subcadena a buscar: ")
    resultado = buscarTodas(cadena, subcadena)
    print("Índices encontrados:")
    print(resultado)
