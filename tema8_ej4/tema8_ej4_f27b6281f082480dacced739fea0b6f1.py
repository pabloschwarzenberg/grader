def rot13(palabra):

    encriptado = ""

    for letra in palabra:

        if letra.isalpha():

            if letra.isupper():

                encriptado += chr((ord(letra) - 65 + 13) % 26 + 65)

            else:

                encriptado += chr((ord(letra) - 97 + 13) % 26 + 97)

        else:

            encriptado += letra

    return encriptado

 

if __name__ == "__main__":

    palabra = input("Ingrese una palabra para encriptar: ")

    print("Palabra encriptada:", rot13(palabra))

           