def jerigonzo(string):
  palabra = ""
  vocales = "aeiou"
  for letra in string:
      if letra in vocales:
        letra = letra + "p" + letra
        palabra = palabra + letra
      else:
        palabra = palabra + letra
  return palabra 

if __name__ == "__main__":
   pass
