def sopaletras(archivo,palabras):
 return palabras
sopa_de_letras =(("C","A","B","L","O","R","O"),
                 ("D","E","B","A","L","L","G"),
                 ("A","A","R","A","L","L","A"),
                 ("V","A","B","D","L","L","T"),
                 ("A","A","L","L","O","L","O"),
                 ("D","G","T","O","R","O","O"),
                 ("C","A","B","A","L","L","O"))
                 
def buscarPorfilas(sopa_de_letras, palabra,filas,columnas):
  f = 0
  while f<filas :
    expresion = ""
    for c in range (0,columnas):
          expresion+=sopa_de_letras[f][c]
    pos=expresion.find(palabra)
    if pos>=0:
     return [f,pos]
    f=f+1
  return None
  
def buscarPorcolumnas(sopa_de_letras, palabra,filas,columnas):
  c = 0
  while c<columnas :
    expresion = ""
    for f in range (0,filas):
          expresion+=sopa_de_letras[f][c]
    pos=expresion.find(palabra)
    if pos>=0:
     return [pos,c]
    c=c+1
  return None
  
def buscarPordiagonales(sopa_de_letras, palabra, filas, columnas):
  for f in range (0,filas):
   for c in range (0,columnas):
    condicion= True
    i=0
    expresion =""
    while f+i<filas and c+i<columnas:
     expresion+=sopa_de_letras[f+i][c+i]
     i=i+1
    pos=expresion.find(palabra)
    if pos>=0:
     return [f+pos,c+pos]
  return None
     
                 

           