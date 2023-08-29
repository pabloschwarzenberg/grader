#Contestador de celular
from time import sleep
n_T = int(input("Ingrese numero telefónico: "))
h_L = int(input("Ingrese hora de llamada: "))
#While true
while True:
    if h_L>=0 and h_L<=7: #Primer If   
        print("CONTESTAR")
        sleep(1)
    if h_L<14:
        if n_T%1000==909:
            print("CONTESTAR")
            sleep(1)
            break
    if h_L>=17 and h_L<=19:
        if n_T//1000==877:
            print("CONTESTAR")
            sleep(1)
            break
    if h_L>19:
        print("NO CONTESTAR")
        break
    else:                    #Else por si ningun if funciona
       print("NO CONTESTAR")
       sleep(1)
       break      