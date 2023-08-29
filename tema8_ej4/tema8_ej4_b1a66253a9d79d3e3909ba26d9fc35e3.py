def rot13(palabra):
    abc = "abcdefghijklmnopqrstuvwxyz"
    Salida_palabra = ""
    for char in palabra:
        Salida_palabra += abc[(abc.find(char)+13)%26]
    return Salida_palabra