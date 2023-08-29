#Cajero Automático
from time import sleep
saldo_del_cajero = 1000000
saldo_del_usuario = 100000
usuario = str((int(input("Ingrese el usuario: "))))
contrasena = str(int(input("Ingrese la contraseña: ")))
while True:
    if usuario == "10334151" and contrasena == "1803":
        print("Usuario y contraseña correctos")
        sleep(1)
        monto_a_retirar = int(input("Ingrese el monto a retirar: "))
        if monto_a_retirar > saldo_del_cajero:
            print("Monto no permitido")
            break
        if monto_a_retirar < saldo_del_usuario and monto_a_retirar < saldo_del_cajero:
            saldo_del_usuario_final = saldo_del_usuario - monto_a_retirar
            saldo_del_cajero_final = saldo_del_cajero - monto_a_retirar
            print("Saldo cuenta="+str(saldo_del_usuario_final))
            print("Saldo cajero="+str(saldo_del_cajero_final))
        if monto_a_retirar != "N":
            break
    if usuario != "10334151" or contrasena != "1803":
        print("Clave invalida")
        sleep(1)
        print("SEGUNDO INTENTO")
        sleep(1)
        contrasena = str(int(input("Ingrese la contraseña nuevamente: ")))
        if usuario != "10334151" or contrasena != "1803":
            print("Clave invalida")
            sleep(1)
            print("TERCER INTENTO")
            sleep(1)
            contrasena = str(int(input("Ingrese la contraseña nuevamente: ")))
            if usuario != "10334151" or contrasena != "1803":
                print("tarjeta bloqueada")
                break
Billetes_20k = int(monto_a_retirar / 20000)
monto_a_retirar = monto_a_retirar % 20000
Billetes_10k = int(monto_a_retirar / 10000)
monto_a_retirar = monto_a_retirar % 10000
Billetes_5k = int(monto_a_retirar / 5000)
monto_a_retirar = monto_a_retirar % 5000

print("Billetes 20000="+str(Billetes_20k))
print("Billetes 10000="+str(Billetes_10k))
print("Billetes 5000="+str(Billetes_5k))