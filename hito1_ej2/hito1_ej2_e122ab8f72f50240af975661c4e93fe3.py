#Contestador de celular
from time import sleep
n = int(input("Ingrese nuemero telefónico: "))
h = int(input("Ingrese hora de llamada: "))

#PRIMER IF
while True:
    if h>=0 and h<=7:
        print("CONTESTAR")
        sleep(1)
    if h<14:
        if n%1000==909:
            print("CONTESTAR")
            sleep(1)
            break
    if h>=17 and h<=19:
        if n//1000==877:
            print("CONTESTAR")
            sleep(1)
            break
    if h>19:
        print("NO CONTESTAR")
        break
    else:
        print("NO CONTESTAR")
        sleep(1)
        break