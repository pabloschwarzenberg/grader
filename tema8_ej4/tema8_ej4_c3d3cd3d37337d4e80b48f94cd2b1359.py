def rot13(palabra):
  encriptada = ""
  for i in palabra:
    if i == "a":
      encriptada += "n"
    if i == "b":
      encriptada += "o"
    if i == "c":
      encriptada += "p"
    if i == "d":
      encriptada += "q"
    if i == "e":
      encriptada += "r"
    if i == "f":
      encriptada += "s"
    if i == "g":
      encriptada += "t"  
    if i == "h":
      encriptada += "u"
    if i == "i":
      encriptada += "v"
    if i == "j":
      encriptada += "w"
    if i == "k":
      encriptada += "x"
    if i == "l":
      encriptada += "y"
    if i == "m":
      encriptada += "z"
    if i== "n":
      encriptada += "a"
    if i =="o":
      encriptada += "b"
    if i == "p":
      encriptada += "c"
    if i == "q":
      encriptada += "d"
    if i =="r":
      encriptada += "e"
    if i== "s":
      encriptada += "f"
    if i =="t":
      encriptada += "g"
    if i =="u":
      encriptada += "h"
    if i =="v":
      encriptada += "i"
    if i =="w":
      encriptada += "j"
    if i =="x":
      encriptada += "k"
    if i =="y":
      encriptada += "l"
    if i =="z":
      encriptada += "m"                        
  return encriptada

           