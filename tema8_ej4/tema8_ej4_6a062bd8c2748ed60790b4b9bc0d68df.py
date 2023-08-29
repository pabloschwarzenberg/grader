def rot13(palabra):
    resultado = ""

    for letra in palabra:
        if letra.isalpha():
            if letra.islower():
                codigo = ord(letra) - ord('a')
                encriptado = (codigo + 13) % 26
                resultado += chr(encriptado + ord('a'))
            else:
                codigo = ord(letra) - ord('A')
                encriptado = (codigo + 13) % 26
                resultado += chr(encriptado + ord('A'))
        else:
            resultado += letra

    return resultado

           