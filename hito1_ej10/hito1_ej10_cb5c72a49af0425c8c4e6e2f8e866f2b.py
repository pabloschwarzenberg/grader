#cajero 1

suario = "10334151"
clave = "1803"
saldo_cajero = 1000000
saldo_cuenta = 100000
intentos = 0
entra = 0
tecla = "N"

while intentos < 3:
    clave_ingresada = input("Ingrese la clave: ")
    intentos = intentos + 1
    if clave_ingresada != clave:
        print("Clave invalida! Intente nuevamente")
    else:
        entra = 1
        break

if entra == 1:
    while tecla == "N":
        retiro = float(input("Monto a retirar: "))
        if retiro > saldo_cuenta:
            print("Monto no permitido!")
        else:
            saldo_cuenta = saldo_cuenta - retiro
            saldo_cajero = saldo_cajero - retiro
            print("Saldo cuenta: " + str(saldo_cuenta))
            print("Saldo cajero: " + str(saldo_cajero))
        tecla = input("Desea realizar otro retiro? N -> Si: ")
else:
    print("Tarjeta bloqueada")