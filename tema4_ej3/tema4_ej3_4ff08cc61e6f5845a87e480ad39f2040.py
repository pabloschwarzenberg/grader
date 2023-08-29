def jerigonzo(string):
    p = ""
    for l in string:
      if l in vocales:
         p += l+"p"+l
      else:
          p += l
    return p

vocales = ["a","e","i","o","u"]

if __name__ == "__main__":
    print(jerigonzo(input("Ingrese una oración a traducir a jerigonzo: ")))
         