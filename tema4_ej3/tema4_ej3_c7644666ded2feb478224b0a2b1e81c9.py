def jerigonzo(string):
    mensaje_final = ""
    vocales = ["a","e","i","o","u"]
    for indice in string:
      if indice in vocales:
          mensaje_final += indice
          mensaje_final += "p"
          mensaje_final += indice
      else:
          mensaje_final += indice
    return mensaje_final

if __name__ == "__main__":
    pass
         