#Cajero Automático
# Definimos las variables iniciales
usuario = 10334151
clave = 1803
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0

while True:
    # Solicitamos el usuario y la clave
    usuario_ingresado = int(input("Ingrese su usuario: "))
    clave_ingresada = int(input("Ingrese su clave: "))

    # Verificamos la clave
    if usuario_ingresado == usuario and clave_ingresada == clave:
        # Solicitamos el monto a retirar
        monto = int(input("Ingrese el monto a retirar: "))

        # Verificamos si el monto es válido
        if monto <= saldo_cuenta and monto <= saldo_cajero:
            # Actualizamos los saldos
            saldo_cuenta -= monto
            saldo_cajero -= monto

            # Imprimimos los nuevos saldos
            print("saldo cuenta=" + str(saldo_cuenta))
            print("saldo cajero=" + str(saldo_cajero))
        else:
            print("monto no permitido")
    else:
        intentos += 1
        if intentos == 3:
            print("tarjeta bloqueada")
            break
        else:
            print("clave invalida")

    # Preguntamos si desea continuar
    continuar = input("¿Desea continuar? (N para salir): ")
    if continuar != "N":
        break
