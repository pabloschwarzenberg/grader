def rot13(palabra):
    palabra2=""
    palabra=palabra.lower()
    for a in palabra:
        if 97<=ord(a)<110:
            palabra2+=chr(ord(a)+13)
        elif 110<=ord(a)<123:
            palabra2+=chr(ord(a)-13)
    return palabra2