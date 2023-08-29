#Cajero Automático
 saldo_cajero = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40
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
            billetes_20000_retiro = min(billetes_20000, monto // 20000)
            billetes_10000_retiro = min(billetes_10000, (monto - billetes_20000_retiro * 20000) // 10000)
            billetes_5000_retiro = min(billetes_5000, (monto - billetes_20000_retiro * 20000 - billetes_10000_retiro * 10000) // 5000)
            saldo_cuenta -= monto
            saldo_cajero -= monto
            billetes_20000 -= billetes_20000_retiro
            billetes_10000 -= billetes_10000_retiro
            billetes_5000 -= billetes_5000_retiro
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero)
            print("Billetes 20000 =", billetes_20000_retiro)
            print("Billetes 10000 =", billetes_10000_retiro)
            print("Billetes 5000 =", billetes_5000_retiro)
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