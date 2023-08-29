#Contestador de celular
from time import sleep
nt = int(input("Ingrese nuemero telefónico: "))
hl = int(input("Ingrese hora de llamada: "))


while True:
    if hl>=0 and hl<=7:
        print("CONTESTAR")
        sleep(1)
    if hl<14:
        if nt%1000==909:
            print("CONTESTAR")
            sleep(1)
            break
    if hl>=17 and hl<=19:
        if nt//1000==877:
            print("CONTESTAR")
            sleep(1)
            break
    if hl>19:
        print("NO CONTESTAR")
        break
    else:
        print("NO CONTESTAR")
        sleep(1)
        break