from time import sleep
usuario = str(int(input("Ingrese el usuario: ")))
contrasena = str(int(input("Ingrese la contraseña: ")))

s_cajero = 1000000
s_usuario = 100000

while True:
    if (usuario == "10334151") and (contrasena == "1803"):
        print("Usuario y contraseña correctos")
        sleep(1)
        monto_a_retirar = int(input("Ingrese el monto a retirar: "))
        if (monto_a_retirar > s_usuario) and (monto_a_retirar > s_cajero):
            print("monto no permitido")
            break
        if (monto_a_retirar < s_usuario) and (monto_a_retirar < s_cajero):
            s_usuario_final = s_usuario-monto_a_retirar
            s_cajero_final = s_cajero-monto_a_retirar
            print("saldo cuenta=", s_usuario_final)
            print("saldo cajero=", s_cajero_final)
        if monto_a_retirar!="N":
            break
    if (usuario != "10334151") or (contrasena != "1803"):
        print("clave invalida")
        sleep(1)
        print("INTENTO N°2")
        sleep(1)
        contrasena = str(int(input("Ingrese la contraseña denuevo: ")))
        if usuario != "10334151" or contrasena != "1803":
            print("clave invalida")
            sleep(1)
            print("INTENTO N°3")
            sleep(1)
            contrasena = str(int(input("Ingrese la contraseña denuevo: ")))
            if usuario != "10334151" or contrasena != "1803":
                print("tarjeta bloqueada")
                break
      