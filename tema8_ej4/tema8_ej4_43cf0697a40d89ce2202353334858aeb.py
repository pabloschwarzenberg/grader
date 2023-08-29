abc = "abcdefghijklmnopqrstuvwxyz"
def rot13(palabra):
    n = 13
    cifrado = ""
    for letra in palabra:
        suma = abc.find(letra) + n
        modulo = int(suma) % len(abc)
        cifrado = cifrado + str(abc[modulo])
    return cifrado

  palabra = input("ingrese la palabra que quiere encriptar: ")
  resultado = rot13(palabra)
  print('el resultado es: ', resultado)abc = "abcdefghijklmnopqrstuvwxyz"
def rot13(palabra):
    n = 13
    cifrado = ""
    for letra in palabra:
        suma = abc.find(letra) + n
        modulo = int(suma) % len(abc)
        cifrado = cifrado + str(abc[modulo])
    return cifrado
if _name_ == "_main_":
  palabra = input("ingrese la palabra que quiere encriptar: ")
  resultado = rot13(palabra)
  print('el resultado es: ', resultado)
           