texto=input("ingrese texto: ")
abc="abcdefghijklmnopqrstuvwxyz"
key=3
cifrado=""

for cifrado in texto:
    if cifrado in abc:
        cifrado+=abc[(abc.index(cifrado)+key)%(len(abc))]

print("el mensaje es:",cifrado)


