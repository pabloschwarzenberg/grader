def jerigonzo(string):
  palabra = ""
  for i in string:
    if i == "a":
      palabra = palabra + i + "pa"
    elif i == "e":
      palabra = palabra + i + "pe"
    elif i == "i":
      palabra = palabra + i + "pi"
    elif i == "o":
      palabra = palabra + i + "po"
    elif i == "u":
      palabra = palabra + i + "pu"
    else:
      palabra = palabra + i
  return palabra
