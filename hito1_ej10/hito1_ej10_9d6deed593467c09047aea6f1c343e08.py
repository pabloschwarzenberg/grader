#Cajero Automático
saldoInicial = 1000000
saldoUsuario = 100000
usuariocorrecto = "10334151"
claveCorrecta = "1803"
intentos = 0

while intentos < 3:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    if usuario == usuariocorrecto and clave == claveCorrecta:
        retiro = float(input("Ingrese el monto a retirar: "))

        if retiro <= saldoUsuario:
            if retiro > 0:
                saldoUsuario -= retiro
                saldoInicial -= retiro
                print("Retiro exitoso")
                print("saldo cuenta= ",saldoUsuario)
                print("saldo cajero= ",saldoInicial)
                break
            else:
                print("Monto no permitido")
        else:
            print("Monto no permitido")
    else:
        print("Clave invalida")
    intentos += 1
    if intentos == 3:
        print("Tarjeta bloqueada")