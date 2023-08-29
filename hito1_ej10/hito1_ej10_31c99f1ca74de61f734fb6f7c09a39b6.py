#Cajero Automático
salir = 'N'
saldoCuenta = 100000
saldoCajero = 1000000
user = 10334151
password = 1803
intentos = 0
while (salir == 'N'):
    input1 = int(input('user: '))
    input2 = int(input('password: '))
    if input1 == user and input2 == password:
        montoRetirar = int(input('Monto a retirar: '))
        saldoCuenta -= montoRetirar
        saldoCajero -= montoRetirar
    else:
        print('clave invalida')
        intentos += 1
    if intentos == 3:
        print('tarjeta bloqueada')
        salir = 'Y'
    print("['saldo cuenta=" + str(saldoCuenta) + "', 'saldo cajero=" + str(saldoCajero) + "']")
    salir = input('¿Salir? ')