def rot13(palabra):
    out_str = ""
    for letra in palabra:
        code = ord(letra)
        if 97 <= code < 110:
            code = code+13
            out_str += chr(code)
        elif 110 <= code < 123:
            code = code-13
            out_str += chr(code)
    return out_str

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           