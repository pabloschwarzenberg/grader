def jerigonzo(string):
    return string
def jerigonzo(palabra):
  i = ""
  for letra in palabra:
    if letra in "aeiouAEIOUáéíóú": 
      i += letra
      i += "p"
    i += letra
  return i
if __name__ == "__main__":
    pass
         