def sopaletras(archivo,palabras):
    archivo=open(archivo,"r")
    tablero=[]
    for linea in archivo:
        linea=linea.replace(" ","")
        linea=linea.replace("\n","")
        linea=linea.upper()
        tablero.append(list(linea))
    filas=len(tablero)
    columnas=len(tablero[0])
    salida=[]
    posicion=0
    for elemento in palabras:
        palabras[posicion]=palabras[posicion].upper()
        posicion+=1
    for palabra in palabras:
        for fila in range(filas-1):
            for columna in range(columnas-1):
                if tablero[fila][columna]==palabra[0]:
                    if buscar_horizontal(tablero,fila,columna,palabra)!="":
                        salida.append(buscar_horizontal(tablero,fila,columna,palabra))
                    if buscar_vertical(tablero,fila,columna,palabra)!="":
                        salida.append(buscar_vertical(tablero,fila,columna,palabra))
                    elif buscar_diagonal(tablero,fila,columna,palabra)!="":
                        salida.append(buscar_diagonal(tablero,fila,columna,palabra))
    return(salida)
                        

def buscar_horizontal(tablero,fila,columna,palabra):
   resultados=""
   i=0
   horizontal=[]
   for letra in palabra:
       try:
           horizontal.append(tablero[fila][columna+i])
           i=i+1
       except IndexError:
           break
   horizontal="".join(horizontal)     
   if palabra=="".join(horizontal):
       resultados=(palabra.lower(),[fila,columna],"derecha")
   return(resultados) 

def buscar_vertical(tablero,fila,columna,palabra):
   resultados=""
   i=0
   vertical=[]
   for letra in palabra:
        try:
            vertical.append(tablero[fila+i][columna])
            i=i+1
        except IndexError:
            break
   if palabra=="".join(vertical):
       resultados=(palabra.lower(),[fila,columna],"abajo")
   return(resultados) 
def buscar_diagonal(tablero,fila,columna,palabra):
   resultados=""
   i=0
   diagonal=[]
   for letra in palabra:
       try:
           diagonal.append(tablero[fila+i][columna+i])
           i=i+1
       except IndexError:
            break
   if palabra=="".join(diagonal):
       resultados=(palabra.lower(),[fila,columna],"diagonal")
   return(resultados)
if __name__=="__main__":
  pass

           