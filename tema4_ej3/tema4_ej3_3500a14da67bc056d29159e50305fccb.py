def jerigonzo(texto):
  resultado = ""
  vocales = "aeiou"

  for letra in texto:
    if letra.lower() in vocales:
      resultado += letra + 'p' + letra.lower()
    else:
      resultado += letra
  return resultado
