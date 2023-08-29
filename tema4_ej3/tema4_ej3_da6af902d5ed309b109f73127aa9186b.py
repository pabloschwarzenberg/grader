def jerigonzo(string):
  palabra =""
  for palabras in range(len(string)):
    if string[palabras] == "a" or string[palabras] == "e" or string[palabras] == "o" or string[palabras] == "i" or string[palabras] == "u":
     palabra += string[palabras]+"p"+string[palabras]
    else:
      palabra += string[palabras]
  return palabra
