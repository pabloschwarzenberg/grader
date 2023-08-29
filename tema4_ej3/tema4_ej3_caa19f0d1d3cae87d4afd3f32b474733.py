def jerigonzo(texto):
  jerigonzo = ""
  
  for letra in texto:
    if letra.lower() in "aeiouáéíóú":
      jerigonzo += letra + "p" + letra.lower()
    else:
      jerigonzo += letra
  return jerigonzo
  
if __name__ == "__main__":
  texto = input("Ingrese un texto:")
  texto_traducido = jerigonzo(texto)
  
  print("Texto traducido al jerigonzo:", texto_traducido)
         