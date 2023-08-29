def rot13(palabra):
     resultado = ""
     for i in range(len(palabra)):
         char = palabra[i]
         resultado += chr((ord(char) + 13 - 97) % 26 + 97)

     return resultado


if __name__ == "__main__":
     palabra = input("Ingresa la palabra que quieras encriptar: ")
     palabra.lower()
     resultado = rot13(palabra)
     print("El resultado es: ", resultado)
           