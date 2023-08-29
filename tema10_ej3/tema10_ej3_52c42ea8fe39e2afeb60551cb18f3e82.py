#Crea un programa capaz de resolver el juego conocido como la sopa de letras. Este juego consiste en un tablero de N x M donde cada posición del tablero tiene una letra. El objetivo del juego es encontrar palabras dentro del tablero, ya sea en forma horizontal (de izquierda a derecha), vertical (de arriba a abajo) o diagonal (de esquina superior izquierda a esquina inferior derecha). Tomando como ejemplo la sopa de letras descrita en este archivo implementa la función sopaletras(nombre_archivo,palabras) que recibe como parámetro el nombre de un archivo con la sopa de letras (en el formato del ejemplo) y una lista de palabras a buscar en la sopa de letras. La función debe retornar una lista de tuplas, con tres valores:
#La palabra tal como la recibe la función en lista de palabras.
#Una lista de dos enteros con la fila y columna inicial donde aparece la palabra
#Un string que describe la dirección en la que aparece la palabra: "derecha", "abajo", "diagonal", de acuerdo a si la palabra aparece en forma horizontal, vertical o diagonal, respectivamente.
#Por ejemplo, la llamada sopaletras("sopa.txt",["casa"]) debería retornar una lista con una tupla de tres elementos: [(casa,[0,0],"derecha")]

def cargar_sopa(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        sopa = [linea.strip().split() for linea in archivo]
    return sopa


def buscar_horizontal(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    palabra = palabra.upper() 
    for fila in range(n_filas):
        for columna in range(n_columnas - len(palabra) + 1):
            if sopa[fila][columna:columna + len(palabra)] == list(palabra):
                return [fila, columna], "derecha"
    return None


def buscar_vertical(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    palabra = palabra.upper() 
    for columna in range(n_columnas):
        for fila in range(n_filas - len(palabra) + 1):
            if [sopa[fila + i][columna] for i in range(len(palabra))] == list(palabra):
                return [fila, columna], "abajo"
    return None

def buscar_diagonal(sopa, palabra):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    palabra = palabra.upper() 
    for fila in range(n_filas - len(palabra) + 1):
        for columna in range(n_columnas - len(palabra) + 1):
            if [sopa[fila + i][columna + i] for i in range(len(palabra))] == list(palabra):
                return [fila, columna], "diagonal"
    return None


def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []
    for palabra in palabras:
        resultado = buscar_horizontal(sopa, palabra)
        if resultado is None:
            resultado = buscar_vertical(sopa, palabra)
        if resultado is None:
            resultado = buscar_diagonal(sopa, palabra)
        if resultado is not None:
            resultados.append((palabra, resultado[0], resultado[1]))
    return resultados



if __name__ == "__main__":
    archivo = "sopa.txt"
    palabras = []
    añadir_palabra = input("Ingrese una palabra: ")
    palabras.append(añadir_palabra)
    resultado = sopaletras(archivo, palabras)
    print(resultado)
