func = "abcdefghijklmnopqrstuvwxyz"
def rot13(palabra):
    texto=""
    for x in palabra:
        suma=func.find(x)+13
        y=int(suma)%len(func)
        texto=texto + str(func[y])
    return texto
z = "hola"
print(rot13(z))
           