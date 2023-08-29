#Contestador de celular
import random as rnd
numero=rnd.randrange(9999999)
hora=rnd.randrange (23)
print({numero})
print({hora})

if 0<= hora <=7:
    print("contestar el telefono")

elif 14 > hora > 7 and numero//100000==909:
    print("contesta el telefono")

elif 14 > hora > 7:
    print("no contesta el telefono")

elif 17>=hora >= 19 and numero//100000 == 877:
    print("no contesta el telefono")

elif 17 <= hora <= 19:
    print("contesta el telefono")

elif hora > 19:
    print("no contesta el telefono")

