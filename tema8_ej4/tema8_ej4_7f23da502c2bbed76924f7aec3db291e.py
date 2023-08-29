def rot13(palabra):
    result = ""
    for char in palabra:
        ascii_val = ord(char)
        if (ascii_val >= ord('a') and ascii_val <= ord('z')):
            result += chr((ascii_val - ord('a') + 13) % 26 + ord('a'))
        elif (ascii_val >= ord('A') and ascii_val <= ord('Z')):
            result += chr((ascii_val - ord('A') + 13) % 26 + ord('A'))
        else:
            result += char
    return result

if __name__=="__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    resultado = rot13(palabra)
    print("El resultado es: ",resultado)
