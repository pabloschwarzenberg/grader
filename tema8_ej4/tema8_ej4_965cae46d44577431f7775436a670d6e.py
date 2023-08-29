def rot13(palabra):
    resultado = ""
    
    for letra in palabra:
        if letra.isalpha():
            if letra.isupper():
                ascii_inicio = ord('A')
            else:
                ascii_inicio = ord('a')
            
            ascii_letra = ord(letra) - ascii_inicio
            ascii_letra_encriptada = (ascii_letra + 13) % 26
            letra_encriptada = chr(ascii_letra_encriptada + ascii_inicio)
            resultado += letra_encriptada
        else:
            resultado += letra
    
    return resultado
          