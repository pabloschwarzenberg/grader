import random
def ocultar_letras(palabra,cantidad):
  palabra = str(palabra)
  cantidad = int(cantidad)
  i = 1
  while i <= cantidad:
    a = random.randint(0,len(palabra)-1)
    if palabra[a] != "_":
      if a != len(palabra):
        palabra = palabra[:a]+ "_"+ palabra[(a+1):]
      else:
        palabra = palabra[0:a]+ "_"
    else:
      continue
    i += 1
  return palabra

def revisar_letra(palabra_secreta,palabra,letra):
  palabra_secreta = str(palabra_secreta)
  palabra = str(palabra)
  letra = str(letra)
  palabra_nueva = ""
  while True:
    if letra in palabra_secreta:
      a = palabra_secreta.find(letra)
      palabra_nueva += palabra[:a]
      palabra_nueva += letra
      palabra_secreta = palabra_secreta[(a + 1):]
      palabra = palabra[(a + 1):]
    else:
      palabra_nueva += palabra
      break
  return palabra_nueva