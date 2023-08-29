#Cajero Automático
saldo_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}

saldo_inicial_usuario = 100000
intentos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Inicio de sesión exitoso.")
        saldo_usuario = saldo_inicial_usuario
        break
    else:
        intentos += 1
        if intentos == 3:
            print("Tarjeta bloqueada. Ha excedido el número de intentos.")
            exit()
        else:
            print("Clave inválida. Intente nuevamente.")

while True:
    monto = float(input("Ingrese el monto a retirar:"))

    if monto <= 0:
        print("Monto no permitido.")
        continue

    if monto > saldo_usuario:
        print("Saldo insuficiente. Su saldo actual es:", saldo_usuario)
    else:
        saldo_usuario -= monto
        print("Retiro exitoso.")
        print("Saldo cuenta =", saldo_usuario)
        
        billetes_entregados = {}
        
        for denominacion, cantidad_disponible in saldo_cajero.items():
            cantidad_billetes = min(int(monto / denominacion), cantidad_disponible)
            monto -= cantidad_billetes * denominacion
            saldo_cajero[denominacion] -= cantidad_billetes
            billetes_entregados[denominacion] = cantidad_billetes
        
        print("Saldo cajero =", saldo_cajero)
        print("Billetes entregados:")
        for denominacion, cantidad in billetes_entregados.items():
            print("Billetes", denominacion, "=", cantidad)

    opcion = input("¿Desea realizar otra transacción? (N para salir): ")
    if opcion.upper() == "N":
        break