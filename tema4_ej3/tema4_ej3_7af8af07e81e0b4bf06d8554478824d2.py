def jerigonzo(string):
  texto = ""
  vocales = ["a", "e", "i", "o", "u"]
  for letra_a_recorrer in string:
    print(letra_a_recorrer)
    if letra_a_recorrer in vocales:
      print(letra_a_recorrer)
      texto += letra_a_recorrer
      texto += "p"
      texto += letra_a_recorrer
    else:
      texto += letra_a_recorrer
  return texto
  print(texto)
print(jerigonzo("hola"))