def validar_clave(usuario, clave):
    if usuario == "10334151" and clave == "1803":
        return True
    else:
        return False

saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if validar_clave(usuario, clave):
        break
    else:
        intentos_fallidos += 1
        print("Clave inválida.")

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada. Intente más tarde.")
        exit()

while True:
    monto_retiro = float(input("Ingrese el monto a retirar: "))

    if monto_retiro > saldo_cuenta:
        print("Monto no permitido. Saldo insuficiente en la cuenta.")
    elif monto_retiro > saldo_cajero:
        print("Monto no permitido. Saldo insuficiente en el cajero.")
    else:
        saldo_cuenta -= monto_retiro
        saldo_cajero -= monto_retiro
        print("['saldo cuenta="+str(int(saldo_cuenta))+"','saldo cajero=", str(int(saldo_cajero))+"']")

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break
