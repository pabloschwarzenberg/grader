def jerigonzo(string):
    nuevoString = ""
    for i in range(len(string)):
      if string[i] in "aeiou":
        nuevoString+=string[i]+"p"+string[i]
      else:
        nuevoString+=string[i]
    string = nuevoString
    return string

if __name__ == "__main__":
    pass
         