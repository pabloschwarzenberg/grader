def jerigonzo(a):
    traducion = ""
    for letra in (a):
        traducion += letra
        if letra.lower() in "aeiou":
            traducion += "p" + letra
    return traducion

  

if __name__=="__main__":
  a= input("Ingrese texto a traducir: ")
  print(jerigonzo(a))