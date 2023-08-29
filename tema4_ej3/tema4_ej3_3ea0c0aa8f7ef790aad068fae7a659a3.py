def jerigonzo(string):
    palabra = []
    palabra =  list(string)
    for letra in palabra:
      if letra == "a":
          palabra.append("pa")
      if letra == "e":
          palabra.append("pe")
      if letra == "i":
          palabra.append("pi")
      if letra == "o":
          palabra.append("po")
      if letra == "u":
          palabra.append("pu")
    print(string)

if __name__ == "__main__":
    pass
         