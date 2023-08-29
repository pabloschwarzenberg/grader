#Cajero Automático
def cajero():
    # Datos de usuario y clave
    usuario_valido = 10334151
    clave_valida = 1803
    intentos = 0

    # Saldo inicial
    saldo_cuenta = 100000
    saldo_cajero = 1000000

    # Validación de usuario y clave
    while True:
        usuario = int(input("Ingrese su número de usuario: "))
        clave = int(input("Ingrese su clave: "))

        if usuario == usuario_valido and clave == clave_valida:
            print("Acceso permitido")
            break
        else:
            intentos += 1
            print("Clave inválida")

        if intentos == 3:
            print("Tarjeta bloqueada")
            return

    # Retiro de dinero
    monto = float(input("Ingrese el monto a retirar: "))

    if monto > saldo_cuenta:
        print("Monto no permitido")
    else:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("Retiro exitoso")
        print(f"Saldo cuenta: {saldo_cuenta}")
        print(f"Saldo cajero: {saldo_cajero}")


# Ejecutar el programa del cajero
cajero()
      