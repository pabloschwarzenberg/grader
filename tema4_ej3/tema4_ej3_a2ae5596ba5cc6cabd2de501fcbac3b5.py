def jerigonzo(palabra):
    traducida = ""
    for letra in palabra:
        traducida += letra
        if letra.lower() in "aeiou":
            traducida += "p" + letra
    return traducida
if __name__ == "__main__":
  palabra = input("Escribe una palabra: ")
  print(jerigonzo(palabra))