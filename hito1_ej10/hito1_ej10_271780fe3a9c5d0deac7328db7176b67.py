#Cajero Automático
saldo_cajero = 1000000
saldo_cuenta = 100000
intentos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Bienvenido.")
        break
    else:
        print("Datos incorrectos.")
        intentos += 1

        if intentos == 3:
            print("Su tarjeta ha sido bloqueada.")
            

while True:
    monto = float(input("Ingrese el monto que desea retirar: "))

    if monto > saldo_cuenta:
        print("El monto no fue permitido. Tiene fondos insuficientes en la cuenta.")
    elif monto > saldo_cajero:
        print("El monto no fue permitido. Tiene fondos insuficientes en el cajero.")
    else:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("Retiro exitoso")
        print(["saldo cuenta={}".format(saldo_cuenta), "saldo cajero={}".format(saldo_cajero)])

    opcion = input("¿Desea realizar alguna operacion mas? (N para salir): ")
    if opcion != "N":
        break      