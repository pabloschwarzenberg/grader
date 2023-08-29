#Cajero Automático
saldo_inicial = 1000000
saldo_usuario = 100000
intentos = 0
continuar = "S"

while continuar == "S":
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        while True:
            monto_retiro = float(input("Ingrese el monto a retirar: "))

            if monto_retiro > saldo_usuario:
                print("Monto no permitido. El saldo actual es:", saldo_usuario)
            else:
                saldo_usuario -= monto_retiro
                saldo_inicial -= monto_retiro
                print("Retiro exitoso. Saldo actual en la cuenta:", saldo_usuario)
                print("Saldo en el cajero:", saldo_inicial)
                break

    else:
        intentos += 1
        print("Clave inválida.")

    if intentos == 3:
        print("Tarjeta bloqueada.")
        break

    continuar = input("¿Desea realizar otra transacción? (S/N): ").upper()

print("Gracias por utilizar nuestro cajero automático. ¡Hasta luego!")
