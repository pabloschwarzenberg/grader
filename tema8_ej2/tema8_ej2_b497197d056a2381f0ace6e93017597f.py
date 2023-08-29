def buscarTodas(a,b):
  contador = 0
  listo = ""
  for letra in a:
    if letra == b:
      listo += str(contador) + " "
    contador += 1
  listo = listo[:-1]
  return listo 

if __name__ == "__main__":
    pass
           