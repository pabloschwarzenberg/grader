def traducir_a_jerigonzo(texto):
  jerigonzo = ""
    for letra in texto:
      if letra.lower() in "aeiouáéíóú":
        jerigonzo += letra + "p" + letra.lower()
      else:
        jerigonzo += letra
    
  return jerigonzo