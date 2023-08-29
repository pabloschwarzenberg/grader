saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Bienvenido, usuario autorizado.")
        saldo_cuenta = 100000
        intentos_fallidos = 0
    else:
        intentos_fallidos += 1
        print("Usuario o clave incorrectos.")
        
        if intentos_fallidos >= 3:
            print("Tarjeta bloqueada. Ha excedido el número máximo de intentos.")
            break

    opcion = input("¿Desea retirar dinero de su cuenta? (S/N): ")

    if opcion.upper() != "S":
        break

    monto = float(input("Ingrese el monto a retirar: "))

    if monto <= saldo_cuenta and monto <= saldo_cajero:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("Retiro exitoso.")
        print(f"Saldo cuenta: {saldo_cuenta}")
        print(f"Saldo cajero: {saldo_cajero}")
    else:
        print("Monto no permitido. Verifique su saldo o el límite del cajero.")

