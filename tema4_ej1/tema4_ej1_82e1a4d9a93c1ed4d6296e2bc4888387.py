from random import randint
def ocultar_letras(palabra,cantidad):
  posFinal = len(palabra)
  palabra = list(palabra)
  for i in range(cantidad):
    palabra[randint(0, posFinal-1)] = '_'
  palabra = ''.join(palabra)
  return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
  if letra in palabra_secreta:
    pos = 0
    palabra = list(palabra)
    for i in palabra_secreta:
      if i == letra:
        palabra[pos] = letra
      pos += 1
    palabra = ''.join(palabra)    
    return palabra
if __name__ == "__main__":
    pass
         