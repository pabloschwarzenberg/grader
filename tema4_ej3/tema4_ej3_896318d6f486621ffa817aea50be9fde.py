def jerigonzo(texto):
  contador = ""
  for x in texto:
    if x in "aeiou":
      contador += x
      contador += "p"
    contador += x
  return contador