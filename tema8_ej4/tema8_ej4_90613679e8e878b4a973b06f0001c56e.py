def rot13(palabra):
    traduccion = ""
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    rot = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"

    for letra in palabra:
        pos = abc.find(letra)
        traduccion += rot[pos]
    return traduccion







           