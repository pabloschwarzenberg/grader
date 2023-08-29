def jerigonzo(string):
  traduccion = []
  for palabra in string:
      for vocales in palabra:
          if vocales in "aeiouAEIOU":
              vocales = vocales + "p"+ vocales
          traduccion.append(vocales)
  traducido = "".join(traduccion)
  return traducido
if __name__=="__main__":
  frase=input("Ingrese la frase a traducir:")
  print(jerigonzo(frase))