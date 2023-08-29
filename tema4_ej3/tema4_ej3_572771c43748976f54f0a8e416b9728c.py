def jerigonzo(string):
    p = ""
    for letra in string:
      if letra in vocales:
         p += letra+"p"+letra
      else:
          p += letra
    return p

vocales = ["a","e","i","o","u"]

if __name__ == "__main__":
    print(jerigonzo(input("Ingrese una oración a traducir a jerigonzo: ")))