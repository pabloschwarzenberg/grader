def rot13(palabra):
    secre = ""
    for i in palabra:
      if i == "a":
       secre += "n"
      if i == "b":
       secre += "o"
      if i == "c":
       secre += "p"
      if i == "d":
       secre += "q"
      if i == "e":
       secre += "r"
      if i == "f":
       secre += "s"
      if i == "g":
       secre += "t"
      if i == "h":
       secre += "u"
      if i == "i":
       secre += "v"
      if i == "j":
       secre += "w"
      if i == "k":
       secre += "x"
      if i == "l":
       secre += "y"
      if i == "m":
       secre += "z"
      if i == "n":
       secre += "a"
      if i == "o":
       secre += "b"
      if i == "p":
       secre += "c"
      if i == "q":
       secre += "d"
      if i == "r":
       secre += "e"
      if i == "s":
       secre += "f"
      if i == "t":
       secre += "g"
      if i == "u":
       secre += "h"
      if i == "v":
       secre += "i"
      if i == "w":
       secre += "j"
      if i == "x":
       secre += "k"
      if i == "y":
       secre += "l"
      if i == "z":
       secre += "m"
      if i == " ":
       secre += " "
    return secre