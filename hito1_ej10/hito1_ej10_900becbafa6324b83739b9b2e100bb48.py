#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_malos = 0

while True:
    usuario = input("Ingrese el usuario: ")
    clave = input("Ingrese la clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Bienvenido al cajero automático")
        break
    else:
        print("clave incorrrecta o usuario")
        intentos_malos += 1

    if intentos_malos == 3:
        print("Tarjeta bloqueada")
        exit()

while True:
    monto = float(input("Ingrese el monto a retirar: "))

    if monto <= 0:
        print("Monto no permitido")
        continue

    if monto > saldo_cuenta:
        print("Saldo insuficiente")
        continue

    if monto > saldo_cajero:
        print("El cajero no tiene suficiente dinero")
        continue

    saldo_cuenta -= monto
    saldo_cajero -= monto

    print("el retiro fue un exito")
    print("Saldo en la cuenta =", saldo_cuenta)
    print("Saldo en cajero =", saldo_cajero)

    opcion = input("¿Desea realizar otra transacción? apreta N para poder salir: ")
    if opcion == "N":
        break      