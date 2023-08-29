saldo_inicial_cajero = 1000000
saldo_inicial_usuario = 100000
intentos_fallidos = 0
clave_valida = False

while True:
    usuario = input("Ingrese su número de usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        clave_valida = True
        saldo_cuenta = saldo_inicial_usuario
        print("Inicio de sesión exitoso.")
        break
    else:
        intentos_fallidos += 1
        print("Clave inválida.")

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada.")
        break

while clave_valida:
    monto_retiro = int(input("Ingrese el monto a retirar: "))

    if monto_retiro <= saldo_cuenta:
        if monto_retiro <= saldo_inicial_cajero:
            saldo_cuenta -= monto_retiro
            saldo_inicial_cajero -= monto_retiro
            print("Retiro exitoso.")
            print("saldo cuenta =", saldo_cuenta)
            print("saldo cajero =", saldo_inicial_cajero)
        else:
            print("Monto no permitido. El saldo en el cajero no es suficiente.")
    else:
        print("Monto no permitido. El saldo en la cuenta no es suficiente.")

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break
