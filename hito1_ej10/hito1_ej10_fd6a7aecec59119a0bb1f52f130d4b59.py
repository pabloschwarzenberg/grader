#Cajero Automático
saldo_inicial = 100000
saldo_cajero = 1000000
intentos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        saldo_cuenta = saldo_inicial

        break
    else:
        intentos += 1
        print("Usuario o clave incorrectos.")

        if intentos >= 3:
            print("Tarjeta bloqueada. Contacte al banco.")
            exit()

while True:
    opcion = input("Desea realizar un retiro? (S/N): ")

    if opcion.upper() != "S":
        break

    monto = float(input("Ingrese el monto a retirar: "))

    if monto <= 0:
        print("Monto no permitido.")
        continue

    if monto > saldo_cuenta or monto > saldo_cajero:
        print("No hay suficiente saldo disponible.")
    else:
        saldo_cuenta -= monto
        saldo_cajero -= monto
     
  

print("Gracias por utilizar el cajero automático.")
