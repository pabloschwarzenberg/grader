def buscarTodas(a, b):
    indices = []  # Lista para almacenar los índices de aparición
    start = 0  # Inicializar el punto de inicio de la búsqueda en 0
    
    while True:
        # Buscar la siguiente aparición de la subcadena b en a, a partir del punto de inicio
        index = a.find(b, start)
        
        # Si no se encontró más ninguna aparición, salir del bucle
        if index == -1:
            break
        
        # Agregar el índice a la lista de índices, convertido a string
        indices.append(str(index))
        
        # Actualizar el punto de inicio para buscar la próxima aparición
        start = index + 1
    
    # Unir los índices en un string separados por espacios y retornarlo
    return ' '.join(indices)


if __name__ == "__main__":
    texto = 'tres tristes tigres'
    subcadena = 't'
    resultado = buscarTodas(texto, subcadena)
    print(resultado)

