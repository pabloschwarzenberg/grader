def rot13(palabra):
  palabra = str(palabra)
  encriptado = ""
  for letra in palabra:
    val_letra = ord(letra)
    if val_letra < 110:
      val_letra += 13
    else:
      val_letra -= 13
    encriptado += chr(val_letra)
  return encriptado
           