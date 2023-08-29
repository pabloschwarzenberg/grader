# Definir una función que reciba dos strings a y b, y retorne un string con los índices de las apariciones de b en a
def buscarTodas(a,b):
    # Crear una lista vacía para guardar los índices
    indices = []
    # Inicializar la posición de búsqueda con 0
    posicion = 0
    # Repetir mientras se encuentre el string b en el string a desde la posición actual
    while b in a[posicion:]:
        # Encontrar el índice de la primera aparición de b desde la posición actual
        indice = a.index(b, posicion)
        # Agregar el índice a la lista
        indices.append(indice)
        # Actualizar la posición de búsqueda con el índice más la longitud de b
        posicion = indice + len(b)
    # Unir los índices de la lista en una sola cadena separada por espacios y retornarla
    return " ".join(str(i) for i in indices)

# Probar la función con algunos ejemplos
if __name__ == "__main__":
    print(buscarTodas("tres tristes tigres", "t")) # Debe imprimir 0 5 9 13
    print(buscarTodas("anita lava la tina", "a")) # Debe imprimir 0 4 8 10 14
    print(buscarTodas("hola mundo", "o")) # Debe imprimir 1 7
