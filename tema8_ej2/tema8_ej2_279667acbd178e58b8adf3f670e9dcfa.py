def buscarTodas(a,b):
    a = a.lower()
    posiciones = ''
    for posicion,letra in enumerate(a):
        if b == letra:
            posiciones += str(posicion) + ' '
    return(posiciones.rstrip(' '))
    
if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    letra = str(input('Ingrese una letra a buscar en la palabra: '))
    print(buscarTodas(palabra, letra))