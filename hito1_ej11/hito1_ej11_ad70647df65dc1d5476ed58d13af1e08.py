from time import sleep

saldo_cajero = 1000000
saldo_usuario = 100000
usuario = str(int(input("Ingrese el usuario: ")))
contraseña = str(int(input("Ingrese la contraseña: ")))

def retirar_dinero():
    monto_a_retirar = int(input("Ingrese el monto a retirar: "))

    if monto_a_retirar > saldo_usuario and monto_a_retirar > saldo_cajero:
        print("Monto no permitido")
        return

    saldo_usuario_final = saldo_usuario - monto_a_retirar
    saldo_cajero_final = saldo_cajero - monto_a_retirar

    print("Saldo cuenta =", saldo_usuario_final)
    print("Saldo cajero =", saldo_cajero_final)

    # Billetes
    b20k = monto_a_retirar // 20000
    monto_a_retirar = monto_a_retirar % 20000
    b10k = monto_a_retirar // 10000
    monto_a_retirar = monto_a_retirar % 10000
    b5k = monto_a_retirar // 5000
    monto_a_retirar = monto_a_retirar % 5000

    print("Billetes de 20000 =", b20k)
    print("Billetes de 10000 =", b10k)
    print("Billetes de 5000 =", b5k)

while True:
    if usuario == "10334151" and contraseña == "1803":
        print("Usuario y contraseña correctos")
        sleep(1)
        retirar_dinero()
        break

    else:
        print("Clave inválida")
        sleep(1)
        print("INTENTO N°1")
        sleep(1)
        print("INTENTO N°2")
        sleep(1)
        print("INTENTO N°3")
        print("Tarjeta bloqueada")
        break
