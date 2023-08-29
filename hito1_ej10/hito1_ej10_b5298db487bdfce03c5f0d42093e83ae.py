#Cajero Automático
contador = 3
cuenta = input("Ingrese su numero de cuenta: ")
while contador > 0:
    password = str(input("Ingrese su contraseña: "))
    if password != "1803":
        print("clave invalida")
        contador = contador -1

    if contador ==0:
        print("tarjeta bloqueada")
    if password == "1803":
        break

SaldoCajero = 1000000
SaldoCuenta = 100000
Attempts = True

while Attempts == True:
    if password == "1803":
     retiro = int(input("Ingrese monto a retirar: "))
    if retiro > 100000:
        print("monto no permitido")
    else:
            NuevoCajero = SaldoCajero - retiro
            NuevaCuenta = SaldoCuenta - retiro
            print("saldo cuenta = ",NuevaCuenta)
            print("saldo cajero = ", NuevoCajero)
            Attempts = False