def rot13(palabra):
      encriptador = 'abcdefghijklmnopqrstuvwxyz'
      texto_cifrado = ''
      d = int(13)
      for letra in palabra:
            suma = encriptador.find(letra) + d
            modulo = int(suma) % len(encriptador)
            texto_cifrado = texto_cifrado + str(encriptador[modulo])
      return texto_cifrado
      pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           