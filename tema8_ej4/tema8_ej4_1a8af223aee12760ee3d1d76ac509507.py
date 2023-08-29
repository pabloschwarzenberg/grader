def rot13(palabra):
  palabra_secreta = ""
  for i in palabra:
    if i == "a":
      palabra_secreta += "n"
    if i == "b":
      palabra_secreta += "o"
    if i == "c":
      palabra_secreta += "p"
    if i == "d":
      palabra_secreta += "q"
    if i == "e":
      palabra_secreta += "r"
    if i == "f":
      palabra_secreta += "s"
    if i == "g":
      palabra_secreta += "t"
    if i == "h":
      palabra_secreta += "u"
    if i == "i":
      palabra_secreta += "v"
    if i == "j":
      palabra_secreta += "w"
    if i == "k":
      palabra_secreta += "x"
    if i == "l":
      palabra_secreta += "y"
    if i == "m":
      palabra_secreta += "z"
    if i == "n":
      palabra_secreta += "a"
    if i == "o":
      palabra_secreta += "b"
    if i == "p":
      palabra_secreta += "c"
    if i == "q":
      palabra_secreta += "d"
    if i == "r":
      palabra_secreta += "e"
    if i == "s":
      palabra_secreta += "f"
    if i == "t":
      palabra_secreta += "g"
    if i == "u":
      palabra_secreta += "h"
    if i == "v":
      palabra_secreta += "i"
    if i == "w":
      palabra_secreta += "j"
    if i == "x":
      palabra_secreta += "k"
    if i == "y":
      palabra_secret += "l"
    if i == "z":
      palabra_secreta += "m"
    if i == " ":
      palabra_secreta += " "
  return palabra_secreta