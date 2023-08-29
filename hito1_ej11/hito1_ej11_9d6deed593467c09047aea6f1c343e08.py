#Cajero Automático
saldoInicial = 1000000
saldoUsuario = 100000
usuariocorrecto = "10334151"
claveCorrecta = "1803"
intentos = 0

billetes20k = 20
billetes10k = 40
billetes5k = 40

while intentos < 3:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    if usuario == usuariocorrecto and clave == claveCorrecta:
        retiro = float(input("Ingrese el monto a retirar: "))
        if retiro <= saldoUsuario:
            if retiro > 0:
                cantidad_billetes20k = 0
                cantidad_billetes10k = 0
                cantidad_billetes5k = 0

            if retiro // 20000 <= billetes20k:
                cantidad_billetes20k = int(retiro // 20000)
                billetes20k -= cantidad_billetes20k
                retiro -= cantidad_billetes20k * 20000

            if retiro // 10000 <= billetes10k:
                cantidad_billetes10k = int(retiro // 10000)
                billetes10k -= cantidad_billetes10k
                retiro -= cantidad_billetes10k * 10000

            if retiro // 5000 <= billetes5k:
                cantidad_billetes5k = int(retiro // 5000)
                billetes5k -= cantidad_billetes5k
                retiro -= cantidad_billetes5k * 5000

            if retiro == 0:
                saldoUsuario -= (cantidad_billetes20k * 20000) + \
                                (cantidad_billetes10k * 10000) + \
                                (cantidad_billetes5k * 5000)
                saldoInicial -= (cantidad_billetes20k * 20000) + \
                                 (cantidad_billetes10k * 10000) + \
                                 (cantidad_billetes5k * 5000)

                print("Retiro exitoso")
                print("saldo cuenta= ", saldoUsuario)
                print("saldo cajero= ", saldoInicial)
                print("Billetes 20000 = ", cantidad_billetes20k)
                print("Billetes 10000 = ", cantidad_billetes10k)
                print("Billetes 5000 = ", cantidad_billetes5k)
                break
            else:
                print("No se pueden distribuir los billetes")
        else:
            print("Monto no permitido")
    else:
        print("Monto no permitido")
else:
    print("Clave invalida")
intentos += 1
if intentos == 3:
    print("Tarjeta bloqueada")