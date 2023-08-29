beta="abcdefghijklmnopqrstuvwxyz"
def rot13(palabra):
    texto_cifrado=""
    for i in palabra:
        suma=beta.find(i) + 13
        mov= int(suma)%len(beta)
        texto_cifrado= texto_cifrado +str(beta[mov])
    return texto_cifrado
c="camioneta"
print(rot13(c))
           