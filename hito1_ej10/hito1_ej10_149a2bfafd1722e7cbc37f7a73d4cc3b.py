#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese el usuario: ")
    clave = input("Ingrese la clave: ")
    
    if usuario == "10334151" and clave == "1803":
        print("Bienvenido/a, usuario válido.")
        break
    else:
        print("Usuario o clave incorrectos.")
        intentos_fallidos += 1
        
    if intentos_fallidos == 3:
        print("Tarjeta bloqueada. Ha excedido el número de intentos.")
        exit()
        
while True:
    monto = float(input("Ingrese el monto a retirar: "))
    
    if monto <= 0 or monto > saldo_cuenta:
        print("Monto no permitido.")
    else:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("Retiro exitoso.")
        print("Saldo cuenta:", saldo_cuenta)
        print("Saldo cajero:", saldo_cajero)
    
    opcion = input("¿Desea realizar otro retiro? (N para salir): ")
    if opcion == "N":
        break
      