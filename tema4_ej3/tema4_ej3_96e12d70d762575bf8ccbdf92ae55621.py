 
def jerigonzo(string):
  texto = ""
  vocal = ["A","a","E","e", "I", "i", "O", "o", "U", "u"]
  for letra in string:
    if letra in vocal:
      texto += letra
      texto += "p"
    texto += letra

  return texto
