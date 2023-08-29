#Cajero Automático


saldo_inicial=1000000
saldo_cuenta=100000
contadorDeIntentosClave=0
usuario = 10334151
clave = 1803

while contadorDeIntentosClave < 4:
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese  su clave: "))

    if usuario == 10334151 and clave == 1803:
        print("Cual es su monto a retirar?")
        montoRetiro = int(input("Ingrese el monto que desea retirar en este cajero automatico: "))
        if montoRetiro <= saldo_cuenta and montoRetiro != 0:
            saldoTotalCuenta = saldo_cuenta - montoRetiro
            saldoTotalCajeroAutomatico = saldo_inicial - montoRetiro
            print("Saldo cuenta = {}".format(saldoTotalCuenta))
            print("Saldo cajero = {}".format(saldoTotalCajeroAutomatico))
            break
        else:
            print("Monto no permitido")
            #volver a pedir montoRetiro

    else:
        print("Clave invalida")
        contadorDeIntentosClave = contadorDeIntentosClave+1
        print(contadorDeIntentosClave)
        if contadorDeIntentosClave == 3:
            print("Tarjeta bloqueada")
            break