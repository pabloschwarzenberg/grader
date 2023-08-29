def rot13(palabra):
    normal = "abcdefghijklmnopqrstuvwxyz"
    clave = "nopqrstuvwxyzabcdefghijklm"
    resultado=''

    for i in range(len(palabra)):
      indiceClave = normal.index(palabra[i])
      resultado += clave[indiceClave]

    return resultado


if __name__ == "__main__":
  palabra = input("Ingresa la palabra que quieras encriptar: ")
  palabra.lower
  resultado  = rot13(palabra)
  print("El resultado es : ",resultado)
