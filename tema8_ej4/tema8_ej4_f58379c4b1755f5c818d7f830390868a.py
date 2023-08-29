def rot13(palabra):
    spin = len(palabra)
    x = 0
    suma = ""
    for i in range(spin):
      palabra[x]
      if palabra[x] == "a" or palabra[x] == "n":
        if palabra[x] == "n":
          suma = suma + "a"
        elif palabra[x] == "a":
          suma = suma + "n"
      elif palabra[x] == "b" or palabra[x] == "o":
        if palabra[x] == "b":
          suma = suma + "o"
        elif palabra[x] == "o":
          suma = suma + "b"
      elif palabra[x] == "c" or palabra[x] == "p":
        if palabra[x] == "c":
          suma = suma + "p"
        elif palabra[x] == "p":
          suma = suma + "c"
      elif palabra[x] == "d" or palabra[x] == "q":
        if palabra[x] == "d":
          suma = suma + "q"
        elif palabra[x] == "q":
          suma = suma + "d"
      elif palabra[x] == "e" or palabra[x] == "r":
        if palabra[x] == "e":
          suma = suma + "r"
        elif palabra[x] == "r":
          suma = suma + "e"
      elif palabra[x] == "f" or palabra[x] == "s":
        if palabra[x] == "f":
          suma = suma + "s"
        elif palabra[x] == "s":
          suma = suma + "f"
      elif palabra[x] == "g" or palabra[x] == "t":
        if palabra[x] == "g":
          suma = suma + "t"
        elif palabra[x] == "t":
          suma = suma + "g"
      elif palabra[x] == "u" or palabra[x] == "h":
        if palabra[x] == "u":
          suma = suma + "h"
        elif palabra[x] == "h":
          suma = suma + "u"
      elif palabra[x] == "i" or palabra[x] == "v":
        if palabra[x] == "i":
          suma = suma + "v"
        elif palabra[x] == "v":
          suma = suma + "i"
      elif palabra[x] == "j" or palabra[x] == "w":
        if palabra[x] == "j":
          suma = suma + "w"
        elif palabra[x] == "w":
          suma = suma + "j"
      elif palabra[x] == "k" or palabra[x] == "x":
        if palabra[x] == "k":
          suma = suma + "x"
        elif palabra[x] == "x":
          suma = suma + "k"
      elif palabra[x] == "l" or palabra[x] == "y":
        if palabra[x] == "l":
          suma = suma + "y"
        elif palabra[x] == "y":
          suma = suma + "l"
      elif palabra[x] == "m" or palabra[x] == "z":
        if palabra[x] == "m":
          suma = suma + "z"
        elif palabra[x] == "z":
          suma = suma + "m"
      x = x + 1
    return suma