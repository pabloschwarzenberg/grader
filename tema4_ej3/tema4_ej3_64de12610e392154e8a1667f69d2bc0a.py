def jerigonzo(string):
  string_copia = ""
  vocales = ["A", "E", "I", "O", "U", "Á", "É", "Í", "Ó", "Ú", "Ü", "a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú", "ü"]
  limite = len(string)
  for i in range(limite):
    if string[i] in vocales:
      string_copia += string[i] + "p" + string[i]
    else:
      string_copia += string[i]
  
  return string_copia
  
if __name__ == "__main__":
  string = str(input("Ingrese el texto: "))
  print(jerigonzo(string))
         