def rot13(s):
    letras = "abcdefghijklmnopqrstuvwxyz"
    palabra = ""
    for i in s.lower():
        palabra += letras[(letras.find(i)+13)%26]
    return palabra
           