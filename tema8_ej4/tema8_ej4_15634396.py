def rot13(palabra):
    ciphertext=''
    for char in palabra:
        code=ord(char)
        if char.isupper():
            code+=13
            if code>ord('Z'):
                code=code-26
        elif char.islower():
            code+=13
            if code>ord('z'):
                code=code-26
        char=chr(code)
        ciphertext+=char
    return ciphertext
if __name__=="__main__":
    palabra=input("Ingresa palabra: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
    
