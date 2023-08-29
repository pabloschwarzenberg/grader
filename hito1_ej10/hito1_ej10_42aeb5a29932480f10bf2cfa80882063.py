#Cajero Automático

def cajero():
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    intentos = 0

    while True:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        if usuario == "10334151" and clave == "1803":
            print("Inicio de sesión exitoso.")
            break
        else:
            intentos += 1
            print("Usuario o clave incorrectos.")

        if intentos == 3:
            print("Tarjeta bloqueada. Contacte al banco.")
            return

    while True:
        monto = int(input("Ingrese el monto a retirar: "))

        if monto > saldo_cuenta:
            print("Monto no permitido. Saldo insuficiente.")
        elif monto > saldo_cajero:
            print("Monto no permitido. Cajero sin suficiente efectivo.")
        else:
            saldo_cuenta -= monto
            saldo_cajero -= monto
        
            print("Saldo cuenta =",saldo_cuenta,"Saldo cajero =", saldo_cajero)
         

        continuar = input("¿salir t ? (S/t): ")
        if continuar.upper() != "t":
            break
