#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0

usuario = "10334151"
clave = "1803"

while True:
    intentos += 1

    if intentos == 4:
        print("Tarjeta bloqueada")
        break

    usuario_ingresado = input("Ingrese su usuario: ")
    clave_ingresada = input("Ingrese su clave: ")

    if usuario_ingresado == usuario and clave_ingresada == clave:
        print("Acceso permitido")
        while True:
            monto = float(input("Ingrese el monto a retirar: "))

            if monto > saldo_cuenta:
                print("Monto no permitido. El saldo de su cuenta es insuficiente.")
            else:
                saldo_cuenta -= monto
                saldo_cajero -= monto
                print("Retiro exitoso.")
                print("Saldo cuenta =", saldo_cuenta)
                print("Saldo cajero =", saldo_cajero)

            opcion = input("¿Desea realizar otro retiro? (N para salir): ")
            if opcion.upper() != "N":
                break

        break
    else:
        print("Clave inválida. Intente nuevamente.")
