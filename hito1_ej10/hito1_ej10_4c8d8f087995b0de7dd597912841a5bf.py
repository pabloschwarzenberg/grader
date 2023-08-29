def validar_clave(usuario, clave):
    if usuario == 10334151 and clave == 1803:
        return True
    else:
        return False

saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

while True:
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))

    if validar_clave(usuario, clave):
        intentos_fallidos = 0
        monto_retiro = float(input("Ingrese el monto a retirar: "))

        if monto_retiro <= saldo_cuenta and monto_retiro <= saldo_cajero:
            saldo_cuenta -= monto_retiro
            saldo_cajero -= monto_retiro
            print("Retiro exitoso.")
            print("Saldo cuenta=", saldo_cuenta)
            print("Saldo cajero=", saldo_cajero)
        else:
            print("Monto no permitido.")
            print("Saldo cuenta=", saldo_cuenta)
            print("Saldo cajero=", saldo_cajero)
    else:
        intentos_fallidos += 1
        print("Clave inválida.")

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada.")
            break

    opcion_salida = input("¿Desea salir? (N para continuar, cualquier otra letra para salir): ")
    if opcion_salida != "N":
        break
