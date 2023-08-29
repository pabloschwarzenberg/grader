def rot13(palabra):
    resultado = []
    for letra in palabra:
        if (ord(letra) < ord("a")+13):
            resultado.append(chr(ord(letra)+13))
        else:
            resultado.append(chr(ord(letra)-13))
    return "".join(resultado)

