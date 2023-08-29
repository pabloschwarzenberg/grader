#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
usuario = "10334151"
clave = "1803"
intentos_fallidos = 0
while True:
    usuario_ingresado = input("Ingrese su usuario: ")
    clave_ingresada = input("Ingrese su clave: ")
    if usuario_ingresado == usuario and clave_ingresada == clave:
        monto = int(input("Ingrese el monto a retirar: "))
        if monto % 5000 != 0 or monto > saldo_cuenta:
            print("Monto no permitido")
        else:
            saldo_cuenta -= monto
            saldo_cajero -= monto
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero)
            intentos_fallidos = 0
    else:
        intentos_fallidos += 1
        if intentos_fallidos == 3:
            print("Tarjeta bloqueada")
            break
        else:
            print("Clave invalida")
    continuar = input("¿Desea continuar? (S/N)").upper()
    if continuar != "S":
        break      