def vocales(texto):
  return texto in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

def jerigonzo(oracion):
  palabra = ''
  for letra in oracion:
    if not vocales (letra):
      palabra += letra
    else:
      palabra += letra + 'p' + letra
  return palabra

    



if __name__ == "__main__":
  pass
         