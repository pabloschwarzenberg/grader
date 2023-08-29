def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.isupper():
                codigo = ord(letra) - ord('A')
                nueva_letra = chr((codigo + 13) % 26 + ord('A'))
            else:
                codigo = ord(letra) - ord('a')
                nueva_letra = chr((codigo + 13) % 26 + ord('a'))
        else:
            nueva_letra = letra
        resultado += nueva_letra
    return resultado

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           