#Contestador de celular
from time import sleep
N_T = int(input("Ingrese nuemero telefónico: "))
H_L = int(input("Ingrese hora de llamada: "))

#FRIST(primer) IF
while True:
    if H_L>=0 and H_L<=7:
        print("CONTESTAR")
        sleep(1)
#second(segunfo) IF       
    if H_L<14:
        if N_T%1000==909:
            print("CONTESTAR")
            sleep(1)
            break
#third(tercer) IF       
    if H_L>=17 and H_L<=19:
        if N_T//1000==877:
            print("CONTESTAR")
            sleep(1)
            break
#fourth(cuarto) IF        
    if H_L>19:
        print("NO CONTESTAR")
        break
    else:
        print("NO CONTESTAR")
        sleep(1)
        break      