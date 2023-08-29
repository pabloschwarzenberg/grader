def jerigonzo(string):
  palabra = ""
  for vocal in string:
    if vocal == "a" or vocal == "A" or vocal == "E" or vocal == "e" or vocal == "i" or vocal == "I" or vocal == "O" or vocal == "o" or vocal == "U" or vocal == "u":
      vocal = vocal + "p" + vocal
      palabra = palabra + vocal
    else:
      palabra = palabra + vocal
  return palabra