# Cajero Automático
saldoICA=1000000
saldoICU=100000
usuario = int(input("Ingrese su usuario: "))
while usuario != 10334151:
    usuario = int(input("Usuario incorrecto, ingrese nuevamente: "))
contraseña = int(input("Ingrese su contraseña: "))
i=0
while contraseña != 1803:
    i = i+1
    if i ==3:
        print("Tarjeta bloqueada")
        break
    else:
        contraseña = int(input("Ingrese nuevamente:"))
if i != 3:
    respuesta = "S"
    while (respuesta == "S"):
        monto= int(input("Ingrese monto que desea retirar:"))
        if monto<=saldoICA:
            if monto<=saldoICU:
                saldoICA = saldoICA - monto
                saldoICU = saldoICU - monto
                print("saldo cuenta=",saldoICU)
                print("saldo cajero=",saldoICA)
            else:
                print("Monto no permitido")
        else:
            print("monto no permitido")

        respuesta = input("Desea realizar otra operacion? (S/N):")
