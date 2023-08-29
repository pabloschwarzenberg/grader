#Cajero Automático
saldo_cajero = 1000000
saldo_cuenta = 100000
usuario = "10334151"
clave = "1803"
intentos = 0

while True:
    print("Bienvenido al cajero automático")
    usuario_ingresado = input("Ingrese su usuario: ")
    clave_ingresada = input("Ingrese su clave: ")
    if usuario_ingresado == usuario and clave_ingresada == clave:
        intentos = 0
        monto = int(input("Ingrese el monto a retirar: "))
        if monto > saldo_cuenta or monto > saldo_cajero:
            print("Monto no permitido")
        else:
            saldo_cuenta -= monto
            saldo_cajero -= monto
            print("Saldo cuenta={}".format(saldo_cuenta))
            print("Saldo cajero={}".format(saldo_cajero))
    else:
        intentos += 1
        if intentos == 3:
            print("Tarjeta bloqueada")
            break
        else:
            print("Clave inválida")
    continuar = input("¿Desea realizar otra operación? (N para salir): ")
    if continuar != "N":
        break


        break
      