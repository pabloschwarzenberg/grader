def LeerSopaLetras(nombre_archivo):
  with open(nombre_archivo, "r") as archivo:
    lista_sopa = archivo.readlines()
    for indice in range(len(lista_sopa)):
      lista_sopa[indice] = lista_sopa[indice].replace("\n","").replace(" ", "").lower()
  return lista_sopa

def BuscarFilaPalabra(palabra, sopa_de_letras):
  
  for fila,linea in enumerate(sopa_de_letras):
    if palabra in linea:
      return fila
  return False 

 
def BuscarPalabra(palabra, sopa_de_letras):
  
  return fila,columna

sopa = LeerSopaLetras("da0Skwiy")
print(BuscarFilaPalabra("cola", sopa))

           