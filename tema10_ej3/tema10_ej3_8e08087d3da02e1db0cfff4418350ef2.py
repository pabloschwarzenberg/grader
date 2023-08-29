Aquí tienes una posible implementación de la función `sopaletras` que resuelve el juego de la sopa de letras:

```python
def cargar_sopa(nombre_archivo):
    sopa = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            sopa.append(fila)
    return sopa

def buscar_horizontal(palabra, sopa):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    
    for i in range(n_filas):
        fila = ''.join(sopa[i])
        if palabra in fila:
            columna_inicial = fila.index(palabra)
            return [i, columna_inicial]
    
    return None

def buscar_vertical(palabra, sopa):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    
    for j in range(n_columnas):
        columna = ''.join([sopa[i][j] for i in range(n_filas)])
        if palabra in columna:
            fila_inicial = columna.index(palabra)
            return [fila_inicial, j]
    
    return None

def buscar_diagonal(palabra, sopa):
    n_filas = len(sopa)
    n_columnas = len(sopa[0])
    
    for i in range(n_filas):
        for j in range(n_columnas):
            # Verificar diagonal hacia abajo y a la derecha
            if i + len(palabra) <= n_filas and j + len(palabra) <= n_columnas:
                diagonal = ''.join([sopa[i+k][j+k] for k in range(len(palabra))])
                if palabra == diagonal:
                    return [i, j]
    
    return None

def sopaletras(nombre_archivo, palabras):
    sopa = cargar_sopa(nombre_archivo)
    resultados = []
    
    for palabra in palabras:
        posicion = buscar_horizontal(palabra, sopa)
        direccion = "derecha"
        
        if posicion is None:
            posicion = buscar_vertical(palabra, sopa)
            direccion = "abajo"
        
        if posicion is None:
            posicion = buscar_diagonal(palabra, sopa)
            direccion = "diagonal"
        
        if posicion is not None:
            resultados.append((palabra, posicion, direccion))
    
    return resultados

if __name__ == "__main__":
    resultados = sopaletras("sopa.txt", ["casa"])
    print(resultados)
```

En esta implementación, se definen varias funciones auxiliares:

1. La función `cargar_sopa` carga la sopa de letras desde un archivo de texto y la devuelve como una lista de listas, donde cada sublista representa una fila de la sopa.

2. Las funciones `buscar_horizontal`, `buscar_vertical` y `buscar_diagonal` buscan una palabra en la sopa de letras en forma horizontal, vertical y diagonal, respectivamente. Devuelven la posición inicial de la palabra si se encuentra, o `None` si no se encuentra.

La función principal `sopaletras` recibe el nombre del archivo con la sopa de letras y una lista de palabras a buscar. Itera sobre cada palabra y utiliza las funciones auxiliares para buscarla en la sopa. Si encuentra la palabra, agrega una tupla con la palabra, la posición inicial y la dirección a una lista de resultados.

Finalmente, se incluye un bloque `if __name__ == "__main__":` para probar la función `sopaletras` con

 el ejemplo proporcionado en el enunciado.
           