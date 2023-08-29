#Cajero Automático
saldo_de_cuenta = 100000
saldo_de_cajero = 1000000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Inicio de sesión exitoso.")
        break
    else:
        print("Usuario o clave incorrectos.")
        intentos_fallidos += 1

        if intentos_fallidos == 3:
            print("Su tarjeta ha sido bloqueada por seguridad.")
            exit()

while True:
    monto = int(input("Ingrese el monto a retirar: "))

    if monto <= saldo_cuenta and monto > 0:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("Retiro exitoso.")
        print("Saldo cuenta:", saldo_cuenta)
        print("Saldo cajero:", saldo_cajero)
    elif monto > saldo_cuenta:
        print("Monto no permitido. Fondos insuficientes.")
    else:
        print("Monto no permitido. Debe ingresar un valor positivo.")

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion != "S":
        break