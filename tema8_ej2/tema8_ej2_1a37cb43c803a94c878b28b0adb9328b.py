def buscarTodas(a, b):
    indices = []  # lista para almacenar los índices encontrados
    pos = 0
    while True:
        # busca la siguiente aparición de b en a, empezando desde pos
        pos = a.find(b, pos)
        if pos == -1:  # si no se encontró más apariciones, termina el ciclo
            break
        indices.append(str(pos))  # agrega la posición encontrada a la lista
        pos += 1  # aumenta la posición inicial para buscar la siguiente aparición
    return " ".join(indices)  # retorna los índices como un solo string separado por espacio

if __name__ == "__main__":
    a = input("Ingrese el string de búsqueda a: ")
    b = input("Ingrese el string a buscar b: ")
    indices_encontrados = buscarTodas(a, b)
    print("Los índices encontrados son:", indices_encontrados)
