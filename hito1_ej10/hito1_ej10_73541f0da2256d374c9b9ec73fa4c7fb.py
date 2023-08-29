def verificar_usuario(usuario, clave):
    if usuario == 10334151 and clave == 1803:
        return True
    else:
        return False

def realizar_retiro(saldo_cuenta, monto):
    if monto > saldo_cuenta:
        return False
    else:
        saldo_cuenta -= monto
        return saldo_cuenta

saldo_cajero = 1000000
saldo_cuenta = 100000

intentos = 0

while True:
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))

    if verificar_usuario(usuario, clave):
        intentos = 0
        monto = int(input("Ingrese el monto a retirar: "))

        if monto <= 0:
            print("Monto no permitido")
        else:
            nuevo_saldo = realizar_retiro(saldo_cuenta, monto)

            if nuevo_saldo is False:
                print("Monto no permitido")
            else:
                saldo_cuenta = nuevo_saldo
                saldo_cajero -= monto
                print("saldo cuenta=",saldo_cuenta)
                print("saldo cajero=",saldo_cajero)

    else:
        intentos += 1
        print("Clave inválida")

    if intentos >= 3:
        print("Tarjeta bloqueada")
        break

    continuar = input("¿Desea realizar otra transacción? (S/N): ")
    if continuar.upper() != "S":
        break