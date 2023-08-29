#Cajero Automático
saldo_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}

saldo_usuario = 100000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Bienvenido/a")
        break
    else:
        print("Usuario o clave incorrectos")
        intentos_fallidos += 1

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada")
            exit()

while True:
    monto_retiro = int(input("Ingrese el monto a retirar: "))

    if monto_retiro > saldo_usuario:
        print("Monto no permitido")
    else:
        billetes_entregados = {}
        saldo_usuario -= monto_retiro

        for denominacion, cantidad in saldo_cajero.items():
            billetes = min(monto_retiro // denominacion, cantidad)
            billetes_entregados[denominacion] = billetes
            monto_retiro -= billetes * denominacion
       