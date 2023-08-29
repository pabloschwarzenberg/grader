#Cajero Automático
      
#Ingreso de datos

saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

#Operacion y respuesta

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        intentos_fallidos = 0
        print("Inicio de sesión exitoso.")
        break
    else:
        intentos_fallidos >= 1
        print("Clave inválida.")

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada.")
        exit()

while True:
    monto = float(input("Ingrese el monto a retirar: "))

    if monto > saldo_cuenta or monto <= 0:
        print("Monto no permitido.")
    else:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("Saldo cuenta: ",(saldo_cuenta))
        print("Saldo cajero: ",(saldo_cajero))

    opcion = input("¿Desea realizar otro retiro? (N para salir): ")
    if opcion.upper() == "N":
        break
