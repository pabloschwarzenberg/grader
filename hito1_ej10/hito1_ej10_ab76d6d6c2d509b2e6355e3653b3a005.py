saldo_cuenta = 100000
saldo_cajero = 1000000

intentos = 0
usuario_valido = False

while intentos < 3 and not usuario_valido:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        usuario_valido = True
        print("¡Bienvenido!")
    else:
        intentos += 1
        print("Clave inválida. Intento {}/3".format(intentos))

if not usuario_valido:
    print("Tarjeta bloqueada")
else:
    opcion = "S"

    while opcion == "S":
        monto = int(input("Ingrese el monto a retirar: "))

        if monto > saldo_cuenta:
            print("Monto no permitido. Saldo insuficiente.")
        elif monto > saldo_cajero:
            print("Monto no permitido. Cajero sin fondos.")
        else:
            saldo_cuenta -= monto
            saldo_cajero -= monto
            print("Retiro exitoso.")
            print("Saldo cuenta={}".format(saldo_cuenta))
            print("Saldo cajero={}".format(saldo_cajero))

        opcion = input("¿Desea hacer otro retiro? (S/N): ")

print("Gracias por utilizar nuestro cajero.")
