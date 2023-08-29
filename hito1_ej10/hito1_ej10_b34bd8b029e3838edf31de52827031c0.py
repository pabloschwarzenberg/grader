#Cajero Automático
cuenta = 100000
cajero = 1000000
intentos = 0

while 1:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Bienvenido")
        break
    else:
        print("Usuario o clave incorrectos")
        intentos += 1
    if intentos == 3:
        print("Tarjeta bloqueada")
        exit()

while 1:
    monto = int(input("Ingrese el monto a retirar: "))

    if monto <= 0:
        print("Monto no permitido")
    elif monto > cuenta or monto > cajero:
        print("Saldo insuficiente")
    else:
        cuenta -= monto
        cajero -= monto
        print("Retiro exitoso")
        print("Saldo cuenta=", cuenta)
        print("Saldo cajero=", cajero)
    respuesta = input("¿Desea realizar otro retiro? (S/N): ")
    if respuesta != "S" and respuesta != "s":
        break
