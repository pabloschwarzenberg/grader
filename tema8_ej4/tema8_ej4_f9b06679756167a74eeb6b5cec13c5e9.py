abc= "abcdefghijklmnopqrstuvwxyz"
def rot13(palabra):
    text_cifrado=""
    for i in palabra:
        suma=abc.find(i) + 13
        mov= int(suma)%len(abc)
        text_cifrado= text_cifrado + str(abc[mov])
    return text_cifrado
c="camioneta"
print(rot13(c))


           