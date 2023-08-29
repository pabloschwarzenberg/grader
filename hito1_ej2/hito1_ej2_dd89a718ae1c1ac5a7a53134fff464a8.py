#Contestador de celular
n = int(input("ingrese un numero con 8 cifras : "))
h = int(input("ingrese la hora de llamada (dos cifras de 0 a 23 horas): "))
inicio = n//100000
final = n % 1000
contesta = True
if(h>=0 and h<=7):
    print("CONTESTAR")

if(h>=8 and h<=14):
    if(final == 909):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")

if(h>14 and h<17):
    print("NO CONTESTAR")

if(h>=17 and h<=19):
    if(inicio == 877):
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")


if(h>=19 and h<=23):
    print("NO CONTESTAR")