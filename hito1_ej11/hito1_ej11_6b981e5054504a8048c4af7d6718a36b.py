from time import sleep

u = str(int(input("Ingrese el usuario: ")))
c = str(int(input("Ingrese la contraseña: ")))

s_cajero = 1000000
s_usuario = 100000

while True:
    if u == "10334151" and c == "1803":
        print("Usuario y contraseña correctos")
        sleep(1)
        monto_a_retirar = int(input("Ingrese el monto a retirar: "))
        if (monto_a_retirar > s_usuario) and (monto_a_retirar > s_cajero):
            print("monto no permitido")
            break
        if (monto_a_retirar < s_usuario) and (monto_a_retirar < s_cajero):
            s_usuario_final = s_usuario - monto_a_retirar
            s_cajero_final = s_cajero-monto_a_retirar
            print("saldo cuenta=", s_usuario_final)
            print("saldo cajero=", s_cajero_final)
            ##Billetes*
            billetes20 = int(monto_a_retirar/20000)
            monto_a_retirar = monto_a_retirar%20000
            billetes10 = int(monto_a_retirar/10000)
            monto_a_retirar = monto_a_retirar%10000
            billetes5 = int(monto_a_retirar/5000)
            monto_a_retirar = monto_a_retirar%5000
            ##Billetes
            print("billetes 20000= ", billetes20)
            print("billetes 10000= ", billetes10)
            print("billetes 5000= ", billetes5)
        if monto_a_retirar!="N":
            break
  
    if u != "10334151" or c != "1803":
        print("clave invalida")
        sleep(1)
        print("INTENTO N°2")
        sleep(1)
        contraseña = str(int(input("Ingrese la contraseña denuevo: ")))
        if usuario != "10334151" or contraseña != "1803":
            print("clave invalida")
            sleep(1)
            print("INTENTO N°3")
            sleep(1)
            contraseña = str(int(input("Ingrese la contraseña denuevo: ")))
            if u != "10334151" or c != "1803":
                print("tarjeta bloqueada")
                break