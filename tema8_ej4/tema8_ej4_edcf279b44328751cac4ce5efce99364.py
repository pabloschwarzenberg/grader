def rot13(palabra):
       palabra2= ""
       for letra in palabra:
            valor = ord(letra)
            if valor <110:
               valor +=13
            else:
                valor -= 13
            palabra2 += chr(valor)
       return palabra2

if __name__=="__main__":
      palabra=input("ingrese una palabra:")
      palabra.lower()
      resultado=rot13(palabra)
      print("el resultado es:",resultado)