#Cajero Automático
j = 0
cajero = 1000000
saldo = 100000
i = 0
while j < 1:
    name = int(input('Ingrese su usuario: '))
    contra = int(input('Ingrese su contrasenna: '))
    if name == 10334151 and contra == 1803:
        while j < 1:
            retiro = int(input('Monto a retirar: '))
            if retiro > 100000 or retiro < 0:
                print("monto invalido")
            else:
                cuenta = saldo - retiro
                sc = cajero - retiro
                b20 = int(retiro / 20000)
                retiro = retiro % 20000
                b10 = int(retiro/10000)
                retiro = retiro % 10000
                b5 = int(retiro / 5000)
                print('saldo cuenta=' + str(cuenta))
                print('saldo cajero=' + str(sc))
                print('billetes 20000=', b20)
                print('billetes 10000=', b10)
                print('billetes 5000=', b5)
                break

        break
    else:
        if i > 2:
            print('tarjeta bloqueada')
            break
        print('clave invalida')
        i = i+1     