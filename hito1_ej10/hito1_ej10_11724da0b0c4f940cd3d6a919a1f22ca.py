#Cajero Automático
from time import sleep
SC = 1000000
SU = 100000
U = str(int(input("Ingrese el usuario: ")))
C = str(int(input("Ingrese la contraseña: ")))

while True:
    if U == "10334151" and C == "1803":
        print("Usuario y contraseña correctos")
        sleep(1)
        M = int(input("Ingrese el monto a retirar: "))
        if M > SU and M > SC:
            print("ERROR: Monto demasiado grande")
            break
        if M < SU and M < SC:
            SU_F = SU - M
            SC_F = SC - M
            print("saldo cuenta=", SU_F)
            print("saldo cajero=", SC_F)
        if M!="N":
            break
    
    if U != "10334151" or C != "1803":
        print("ERROR: Clave incorrecta")
        sleep(1)
        print("INTENTO N°2")
        sleep(1)
        C = str(int(input("Ingrese la contraseña: ")))
        if U != "10334151" or C != "1803":
            print("ERROR: Clave incorrecta ")
            sleep(1)
            print("INTENTO N°3")
            sleep(1)
            C = str(int(input("Ingrese la contraseña: ")))
            if U != "10334151" or C != "1803":
                print("ERROR: La tarjeta ha sido bloqueada")
                break