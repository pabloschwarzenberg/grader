def rot13(palabra):
    string = ""
    for letra in palabra:
      if ord(letra) >= ord('n'):
        string += chr(ord(letra) - 13)
      else:
        string += chr(ord(letra) + 13)
    return string

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           