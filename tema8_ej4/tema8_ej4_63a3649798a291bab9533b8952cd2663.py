
 texto=input("tu texto:")

if texto==texto.upper():
    abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
else:
    abc="abcdefghijklmnñopqrstuvwxyz"

k=int(input("ingresa la plabra que quieras encriptar:" ))
cifrad=""

for c in texto:
    if c in abc:
        cifrad += abc[(abc.index(c)%(len(abc))]
    else:
        cifrad+=c
print("el resultado es: ",resultado)


              
         