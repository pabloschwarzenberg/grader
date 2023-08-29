def rot13(palabra):
    encriptando = palabra.translate(palabra.maketrans(letras,cambiodeletras))
    print(encriptando)

letras ="abcdefghijklmnopqrstuvwxyz"
cambiodeletras="nopqrstuvwxyzabcdefghijklm"
palabra = input("ingrese una palabra o mensaje:")
resultado = rot13(palabra)
print(resultado)
           