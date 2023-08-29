import codecs
def rot13(palabra):
  modified=codecs.encode(palabra, "rot_13")
  return modified
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           