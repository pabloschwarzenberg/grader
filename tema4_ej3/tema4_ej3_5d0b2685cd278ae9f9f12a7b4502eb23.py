def jerigonzo(string):
    vocales=["a","e","i","o","u"]
    palabra=""
    for i in string:
      if i in vocales:
        palabra=palabra+i+"p"+i
      else:
        palabra=palabra+i
    return palabra

if __name__ == "__main__":
    pass
         