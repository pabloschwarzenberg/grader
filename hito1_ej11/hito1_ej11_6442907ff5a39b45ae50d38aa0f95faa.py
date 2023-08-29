def validar_clave(usuario, clave):
    if usuario == "10334151" and clave == "1803":
        return True
    else:
        return False

saldo_cuenta = 100000
saldo_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if validar_clave(usuario, clave):
        intentos_fallidos = 0
        monto_retiro = float(input("Ingrese el monto a retirar: "))

        if monto_retiro <= saldo_cuenta and monto_retiro <= sum([valor * cantidad for valor, cantidad in saldo_cajero.items()]):
            billetes_entregados = {}

            for valor, cantidad in saldo_cajero.items():
                cantidad_billetes = min(cantidad, int(monto_retiro / valor))
                monto_retiro -= valor * cantidad_billetes
                billetes_entregados[valor] = cantidad_billetes
                saldo_cajero[valor] -= cantidad_billetes

            saldo_cuenta -= monto_retiro

            print("Retiro exitoso")
            print("Billetes entregados:")
            for valor, cantidad in billetes_entregados.items():
                print(f"billetes {valor} = {cantidad}")
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
print("Saldo cajero:")
for valor, cantidad in saldo_cajero.items():
    print(f"billetes {valor} = {cantidad}")
