#Contestador de celular
from time import sleep
t = int(input("Ingrese numero telefónico: "))
l = int(input("Ingrese hora de llamada: "))

while True:
    if l>=0 and l<=7:
        print("CONTESTAR")
        sleep(1)
    if l<14:
        if t%1000==909:
            print("CONTESTAR")
            sleep(1)
            break
    if l>=17 and l<=19:
        if t//1000==877:
            print("CONTESTAR")
            sleep(1)
            break
    if l>19:
        print("NO CONTESTAR")
        break
    else:
        print("NO CONTESTAR")
        sleep(1)
        break