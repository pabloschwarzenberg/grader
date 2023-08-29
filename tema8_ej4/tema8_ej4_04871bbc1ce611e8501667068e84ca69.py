abc = "abcdefghijklmnopqrstuvwxyz"
def rot13(palabra):
    text=""
    for i in palabra:
        suma=abc.find(i)+13
        m=int(suma)%len(abc)
        text=text + str(abc[m])
    return text
           