def jerigonzo(string):
  Jerigonzo = []
  for palabra in string:
    for letra in palabra:
      if letra in "aeiou":
        letra = letra + "p"+ letra
      Jerigonzo.append(letra)
  Jerigonzo = "".join(Jerigonzo)
  return Jerigonzo