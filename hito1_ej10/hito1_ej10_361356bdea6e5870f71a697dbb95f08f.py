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
            if retiro > saldo or retiro < 0:
                print("monto invalido")
            else:
                saldo = saldo - retiro
                cajero = cajero - retiro
                print('saldo cuenta=' + str(saldo))
                print('saldo cajero=' + str(cajero))
                break

        break
    else:
        if i > 1:
            print('tarjeta bloqueada')
            break
        print('clave invalida')
        i = i+1