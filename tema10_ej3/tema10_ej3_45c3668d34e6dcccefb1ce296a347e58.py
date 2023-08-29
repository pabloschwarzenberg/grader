def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    archivo.close()
    return [(palabras[0],[0,0],"diagonal")]

if __name__ == "__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))
def sopaletras(nombre_archivo, palabras):

    m = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = linea.strip().split()
            m.append(fila)
    
    filas = len(m)
    columnas = len(m[0])
    
    r = []
    

    def buscar_palabra(palabra, fila_inicial, col_inicial, dir_fila, dir_col):
        fila_actual = fila_inicial
        col_actual = col_inicial
        
        for letra in palabra:
            if fila_actual < 0 or fila_actual >= filas or col_actual < 0 or col_actual >= columnas or m[fila_actual][col_actual].lower() != letra:
                return False
            fila_actual += dir_fila
            col_actual += dir_col
        
        return True
    

    def determinar_direccion(fila_inicial, col_inicial, fila_final, col_final):
        if fila_inicial == fila_final:
            return "derecha"
        elif col_inicial == col_final:
            return "abajo"
        else:
            return "diagonal"
    

    for palabra in palabras:
        palabra = palabra.lower()  
        
        for fila in range(filas):
            for col in range(columnas):
                if buscar_palabra(palabra, fila, col, 0, 1): 
                    direccion = determinar_direccion(fila, col, fila, col+len(palabra)-1)
                    r.append((palabra, [fila, col], direccion))
                
                if buscar_palabra(palabra, fila, col, 1, 0):  
                    direccion = determinar_direccion(fila, col, fila+len(palabra)-1, col)
                    r.append((palabra, [fila, col], direccion))
                
                if buscar_palabra(palabra, fila, col, 1, 1):  
                    direccion = determinar_direccion(fila, col, fila+len(palabra)-1, col+len(palabra)-1)
                    r.append((palabra, [fila, col], direccion))
    
    return r


if __name__ == "__main__":
    resultado = sopaletras("sopa.txt", ["casa", "cra", "aro"])