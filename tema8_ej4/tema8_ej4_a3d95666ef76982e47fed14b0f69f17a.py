def rot13(palabra):
    encrypted_palabra = ""
    pass
    for char in palabra:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            rotated_ascii = (ord(char) - ascii_offset + 13) % 26 + ascii_offset
            encrypted_palabra += chr(rotated_ascii)
        else:
            encrypted_palabra += char
    return encrypted_palabra
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           