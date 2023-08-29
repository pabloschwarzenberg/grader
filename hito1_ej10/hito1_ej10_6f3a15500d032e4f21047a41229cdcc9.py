saldo_inicial = 1000000
saldo_cuenta = 100000
saldo_cajero = saldo_inicial

intentos = 0
bloqueado = False
while True:
    ingreso_usuario = input("Ingrese el usuario: ")
    ingreso_clave = input("Ingrese la clave: ")

    if ingreso_usuario == usuario and ingreso_clave == clave:
        print("Bienvenido al Cajero Automático")
        break
    else:
        intentos_fallidos += 1
        if intentos_fallidos == 3:
            print("Tarjeta Bloqueada")
            exit()
        else:
            print("Clave Invalida, Intente Nuevamente")
 monto = float(input("Ingrese el monto a retirar: "))

            if monto <= 0:
                print("Monto no permitido.")
            elif monto > saldo_cuenta:
                print("Saldo insuficiente.")
            elif monto > saldo_cajero:
                print("No hay suficiente dinero en el cajero.")
            else:
                saldo_cuenta -= monto
                saldo_cajero -= monto
                print("Retiro exitoso.")
                print("Saldo cuenta =", saldo_cuenta)
                print("Saldo cajero =", saldo_cajero)

            respuesta = input("¿Desea realizar otro retiro? (S/N): ")
            if respuesta.upper() != "S":
                print("Programa finalizado.")
                break
    else:
        intentos += 1
        print("Clave inválida.")
        if intentos == 3:
            bloqueado = True
            print("Tarjeta bloqueada. Programa finalizado.")
            break
