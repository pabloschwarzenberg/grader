#Cajero Automático
#ENTRADA

NumUsuario = int(input("Ingrese el número de usuario: "))

Clave = int(input("Ingrese la clave: "))

#VARIABLES TEMPORALES
Usuario = "N"

SaldoCajero = 1000000

SaldoUsuario = 100000

Intentos = 1

#PROCESO

while Usuario == "N":
    if NumUsuario == 10334151 and Clave == 1803:
        Monto=int(input("Ingese el monto a retirar: "))
        if Monto > SaldoUsuario:
            print("Monto no permitido")


        elif Monto <= SaldoUsuario:
            SaldoCajero = SaldoCajero - Monto
            SaldoUsuario = SaldoUsuario - Monto
            print("Saldo cuenta =" + str(SaldoUsuario))
            print("Saldo cajero =" + str(SaldoCajero))
            Salir = str(input("Ingrese una letra distinta a N" + " para salir: "))

            if Salir != "N":
                Usuario = Salir


    elif Clave != 1803 and Intentos != 3:
        print("Clave invalida")
        Clave = int(input("Ingrese la clave: "))
        Intentos +=1

    if Intentos == 3:
        print("Tarjeta bloqueada")
        Salir = str(input("Ingrese una letra distinta a N" + " para salir: "))

        if Salir != "N":
            Usuario = Salir      