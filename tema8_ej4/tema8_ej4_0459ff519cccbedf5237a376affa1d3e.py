#encriptador
def rot13(palabra):
    encriptador =""
    palabra1 = palabra.lower()
    letras = "abcdefghijklmnopqrstuvwxyz"
    letras1 = "nopqrstuvwxyzabcdefghijklm"
    for i in palabra1:
        if i in letras:
            pos = letras1[letras.find(i)]
            encriptador = encriptador + pos
    return encriptador
           