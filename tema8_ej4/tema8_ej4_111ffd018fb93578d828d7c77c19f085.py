abc = "abcdefghijklmnopqrstuvwxyz"
def rot13(palabra):
    text=""
    for e in palabra:
        cambio=abc.find(e)+13
        n=int(cambio)%len(abc)
        text=text + str(abc[n])
    return text


c = "hola"
print(rot13(c))
           