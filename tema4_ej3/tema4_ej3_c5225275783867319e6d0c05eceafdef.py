def jerigonzo(string):
  string_jerigonzo = ""
  vocales = "aeiouAEIOU"

  for letra in string:
   if letra in vocales:
     string_jerigonzo += letra + "p" + letra.lower()
   else:
     string_jerigonzo += letra
    
  return string_jerigonzo

if __name__ == "__main__":
  string_original = input("Ingrese un texto: ")
  string_traducido = jerigonzo(string_original)
  print("Texto traducido a jerigonzo:", string_traducido)
         