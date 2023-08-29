saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

resultado = []

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        resultado.append("Inicio de sesión exitoso.")
        break
    else:
        resultado.append("Usuario o clave incorrectos.")
        intentos_fallidos += 1

        if intentos_fallidos == 3:
            resultado.append("Tarjeta bloqueada. Contacte al banco.")
            break

while True:
    monto_retiro = float(input("Ingrese el monto a retirar: "))

    if monto_retiro > saldo_cuenta or monto_retiro > saldo_cajero:
        resultado.append("Monto no permitido. Verifique su saldo.")
    else:
        saldo_cuenta -= monto_retiro
        saldo_cajero -= monto_retiro
        resultado.append("Retiro exitoso.")
        resultado.append("Saldo cuenta=" + str(saldo_cuenta))
        resultado.append("Saldo cajero=" + str(saldo_cajero))

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion != "S":
        break

print(resultado)