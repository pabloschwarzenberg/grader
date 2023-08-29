#Cajero Automático
      saldo_inicial = {
    20000: 20,
    10000: 40,
    5000: 40
}

saldo_cuenta = 100000
saldo_cajero = sum(valor * cantidad for valor, cantidad in saldo_inicial.items())

continuar = True

while continuar:
    intentos = 0
    usuario_valido = False

    while intentos < 3 and not usuario_valido:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        if usuario == "10334151" and clave == "1803":
            usuario_valido = True
        else:
            print("Usuario o clave incorrectos. Intente nuevamente.")
            intentos += 1

    if intentos == 3:
        print("Tarjeta bloqueada.")
        break

    monto_retiro = float(input("Ingrese el monto a retirar: "))

    if monto_retiro <= saldo_cuenta:
        if monto_retiro <= saldo_cajero:
            billetes_entregados = {}

            for valor, cantidad in saldo_inicial.items():
                billetes_necesarios = min(monto_retiro // valor, cantidad)
                billetes_entregados[valor] = billetes_necesarios
                monto_retiro -= billetes_necesarios * valor
