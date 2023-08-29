def rot13(palabra):
    rot_13 = "abcdefghijklmnopqrstuvwxyz"
    transcribir = rot_13[13:] + rot_13[:13]
    rot_13_char = lambda c: transcribir[rot_13.find(c)] if rot_13.find(c) > -1 else c
    return ''.join(rot_13_char(c) for c in palabra)

    pass

if __name__== "__main_":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
