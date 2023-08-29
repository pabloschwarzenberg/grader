def rot13(palabra):
    chars = "abcdefghijklmnopqrstuvwxyz"
    trans = chars[13:]+chars[:13]
    rot_char = lambda c: trans[chars.find(c)] if chars.find(c)>-1 else c
    return ''.join( rot_char(c) for c in palabra )

if __name__=="__main__":
    palabra=input("Ingrese la palabra que quiere encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ", resultado)