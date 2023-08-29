#Cajero Automático
saldo_inicial = 1000000
saldo_cuenta = 100000
saldo_cajero = saldo_inicial - saldo_cuenta
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Bienvenido")
        break
    else:
        intentos_fallidos += 1
        print("Clave inválida")

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada")
            exit()

while True:
    monto_retiro = float(input("Ingrese el monto a retirar: "))

    if monto_retiro <= saldo_cuenta:
        if monto_retiro > saldo_cajero:
            print("Monto no permitido")
        else:
            saldo_cuenta -= monto_retiro
            saldo_cajero -= monto_retiro
            print("saldo cuenta =", saldo_cuenta)
            print("saldo cajero =", saldo_cajero)
    else:
        print("Monto no permitido")

    opcion = input("¿Desea hacer otro retiro? (S/N): ")

    if opcion.upper() != "S":
        break
