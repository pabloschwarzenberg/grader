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
        intentos_fallidos = 0
        monto_retiro = float(input("Ingrese el monto a retirar: "))

        if monto_retiro <= saldo_cuenta and monto_retiro <= saldo_cajero:
            saldo_cuenta -= monto_retiro
            saldo_cajero -= monto_retiro
            print("Retiro exitoso")
        else:
            print("Monto no permitido")
    else:
        intentos_fallidos += 1
        print("Clave inválida")

    if intentos_fallidos >= 3:
        print("Tarjeta bloqueada")
        break

    respuesta = input("¿Desea realizar otra operación? (N para salir): ")
    if respuesta == "N":
        break

print(f"Saldo cuenta: {saldo_cuenta}")
print(f"Saldo cajero: {saldo_cajero}")