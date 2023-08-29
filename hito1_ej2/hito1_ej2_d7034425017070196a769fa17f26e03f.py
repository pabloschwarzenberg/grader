#Contestador de celular
from time import sleep
n_T = int(input("ingrese número telefónico: "))
h_L = int(input("ingrese hora de llamada: "))

while True:
    if h_L>=0 and h_L<=7:
        print("CONTESTAR")
        sleep(1)
    if h_L<14:
        if n_T%1000==909:
            print("CONTESTAR")
            sleep(1)
            break
    if h_L>19:
        print("NO CONTESTAR")
        break
    else:
        print("NO CONTESTAR")
        sleep(1)
        break