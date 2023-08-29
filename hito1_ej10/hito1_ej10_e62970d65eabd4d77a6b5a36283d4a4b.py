saldo_cuenta = 100000
saldo_cajero = 1000000
contador = 0

opcion = "N"

while opcion == "N":
    usuario = input("Ingrese usuario")
    clave = input("Ingrese contraseña")

    if(usuario=="10334151" and clave == "1803"):
        giro = int(input("Ingrese un giro"))
        if(giro<saldo_cajero):
                    if(giro<saldo_cuenta):
                        saldo_cajero = saldo_cajero-giro
                        saldo_cuenta = saldo_cuenta - giro
                        print("Saldo Cuenta=", saldo_cuenta)
                        print("Saldo Cajero=", saldo_cajero)
                        opcion = input("Ingrese N para continuar: ")
                    else:
                        print("Saldo insuficiente")
        else:
            print("Saldo insuficiente")
    if(clave != "1803"):
        print("Clave inválida")
        contador += 1
        if(contador==3):
            print("tarjeta bloqueadas")
            break