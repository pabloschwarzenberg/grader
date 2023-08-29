def rot13(palabra):
  secret = ""
  for i in palabra:
    if i == "a":
      secret += "n"
    if i == "b":
      secret += "o"
    if i == "c":
      secret += "p"
    if i == "d":
      secret += "q"
    if i == "e":
      secret += "r"
    if i == "f":
      secret += "s"
    if i == "g":
      secret += "t"
    if i == "h":
      secret += "u"
    if i == "i":
      secret += "v"
    if i == "j":
      secret += "W"
    if i == "k":
      secret += "x"
    if i == "l":
      secret += "y"
    if i == "m":
      secret += "z"
    if i == "n":
      secret += "a"
    if i == "o":
      secret += "b"
    if i == "p":
      secret += "c"
    if i == "q":
      secret += "d"
    if i == "r":
      secret += "e"
    if i == "s":
      secret += "f"
    if i == "t":
      secret += "g"
    if i == "u":
      secret += "h"
    if i == "v":
      secret += "i"
    if i == "w":
      secret += "j"
    if i == "x":
      secret += "k"
    if i == "y":
      secret += "l"
    if i == "z":
      secret += "m"
    if i == " ":
      secret += " "
  return secret

