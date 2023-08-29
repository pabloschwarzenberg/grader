def jerigonzo(string):
    mensaje = ""
    vocales = ["a","e","i","o","u"]
    for index in string:
      if index in vocales:
          mensaje += index
          mensaje += "p"
          mensaje += index
      else:
          mensaje += index
    return mensaje

if __name__ == "__main__":
    pass
         