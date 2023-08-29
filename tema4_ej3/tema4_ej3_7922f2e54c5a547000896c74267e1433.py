def jerigonzo(string):
    return string

if __name__ == "__main__":
    pass
def jerigonzo(palabra):
  i = ""
  for letter in palabra:
    if letter in "AEIOUaeiouáéíóú": 
      i += letter
      i += "p"
    i += letter
  return i