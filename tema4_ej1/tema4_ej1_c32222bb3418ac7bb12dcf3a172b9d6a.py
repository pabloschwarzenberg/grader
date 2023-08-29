def ocultar_letras(palabra,cantidad):
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    return palabra

if __name__ == "__main__":
    pass
 palabras=['perro','hormiga','zorro','gato','loro']

def buscarTodas(a,b):
  index = []
  start = 0
  end = len(a)
  lista = list(a)
while True:
  try:
  pos = lista.index(b, start, end)
  index.append(pos)
  start = pos + 1
  except ValueError:
  break

 return index
