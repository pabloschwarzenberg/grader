def rot13(palabra):
    encriptada = ""
    
    for letra in palabra:
        if letra.isalpha():
            ascii_val = ord(letra.lower())
            if ascii_val >= 97 and ascii_val <= 109:
                encriptada += chr(ascii_val + 13)
            elif ascii_val >= 110 and ascii_val <= 122:
                encriptada += chr(ascii_val - 13)
            else:
                encriptada += letra
        else:
            encriptada += letra
    
    return encriptada
