#Cajero Automático
saldo_inicial = 1000000
saldo_cajero = 1000000
intentos_fallidos = 0
clave_valida = False

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        saldo_cuenta = 100000
        clave_valida = True
        break
    else:
        print("Clave inválida")
        intentos_fallidos += 1

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada")
        exit()

while True:
    if clave_valida:
        monto_retiro = int(input("Ingrese el monto a retirar: "))

        if monto_retiro > saldo_cuenta or monto_retiro < 0:
            print("Monto no permitido")
        else:
            saldo_cuenta -= monto_retiro
            saldo_cajero -= monto_retiro
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero)

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break
 