def LeerSopaLetras(nombre_archivo):
  with open(nombre_archivo, "r") as archivo:
    lista_sopa = archivo.readlines()
    for indice in range(len(lista_sopa)):
      lista_sopa[indice] = lista_sopa[indice].replace("\n","").replace(" ", "").lower()
  return lista_sopa

def BuscarFilaPalabra(palabra, sopa_de_letras):
  # esta funcion retornará la linea (fila) en la que está la palabra. Si no está la palabra retornará False
  for fila,linea in enumerate(sopa_de_letras):
    if palabra in linea:
      return fila
  return False # en este punto ya recorrio todas las filas sin encontrar la palabra

# BuscarFilaPalabra solo retorna la fila donde está la palabra,
# pero no retorna la columna. Haremos una función que retorne la fila y columna 
# de la palabra 
def BuscarPalabra(palabra, sopa_de_letras):
  # escriba su codigo
  # se recomienda usar slices [desde:hasta] con el largo del string a buscar
  # debemos identificar donde parte
  # --------- COMPLETE
  return fila,columna

sopa = LeerSopaLetras("da0Skwiy")    
print(BuscarFilaPalabra("cola", sopa))