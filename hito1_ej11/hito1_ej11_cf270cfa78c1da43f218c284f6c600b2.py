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

    if monto <= saldo_cuenta and monto <= sum(k * v for k, v in saldo_cajero.items()):
        saldo_cuenta -= monto
        print("Retiro exitoso.")

        billetes_entregados = {}

        for billete, cantidad in sorted(saldo_cajero.items(), reverse=True):
            if monto >= billete and cantidad > 0:
                num_billetes = min(monto // billete, cantidad)
                billetes_entregados[billete] = num_billetes
                monto -= billete * num_billetes
                saldo_cajero[billete] -= num_billetes

        print(f"Saldo cuenta: {saldo_cuenta}")
        print(f"Saldo cajero: {saldo_cajero}")

        print("Billetes entregados:")
        for billete, cantidad in billetes_entregados.items():
            print(f"billetes {billete} = {cantidad}")
    else:
        print("Monto no permitido. Verifique su saldo o el límite del cajero.")