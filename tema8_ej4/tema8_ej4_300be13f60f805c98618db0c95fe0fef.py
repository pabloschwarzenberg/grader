def rot13(palabra):
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
      
def rot13(word):
    encrypted = ""
    for char in word:
        if char.isalpha():
            if char.isupper():
                encrypted += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            else:
                encrypted += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        else:
            encrypted += char
    return encrypted
