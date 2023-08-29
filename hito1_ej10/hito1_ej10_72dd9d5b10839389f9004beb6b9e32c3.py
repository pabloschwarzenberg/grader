def cajero():
    usuario_valido = 10334151
    clave_valida = 1803
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    intentos_fallidos = 0

    while True:
        usuario = int(input("Ingrese su usuario: "))
        clave = int(input("Ingrese su clave: "))

        if usuario == usuario_valido and clave == clave_valida:
            print("Acceso permitido")
            break
        else:
            intentos_fallidos += 1
            print("Clave inválida")
            if intentos_fallidos == 3:
                print("Tarjeta bloqueada")
                return

    while True:
        monto_retiro = float(input("Ingrese el monto a retirar: "))

        if monto_retiro > saldo_cuenta:
            print("Monto no permitido. Saldo insuficiente.")
        elif monto_retiro > saldo_cajero:
            print("Monto no permitido. Saldo del cajero insuficiente.")
        else:
            saldo_cuenta -= monto_retiro
            saldo_cajero -= monto_retiro
            print("Retiro exitoso")
            print("Saldo cuenta:", saldo_cuenta)
            print("Saldo cajero:", saldo_cajero)

        opcion = input("¿Desea realizar otro retiro? (S/N): ")
        if opcion.upper() != "S":
            break

if __name__ == "__main__":
    cajero()


      