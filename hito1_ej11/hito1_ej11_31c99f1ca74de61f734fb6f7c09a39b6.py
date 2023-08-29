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
    billetes20000 = 0
    billetes10000 = 0
    billetes5000 = 0
    substraction = 0
    aux = montoRetirar
    while (montoRetirar != 0):
        if aux >= substraction+20000:
            substraction += 20000
            montoRetirar -= 20000
            billetes20000 += 1
        if aux >= substraction+10000:
            substraction += 10000
            montoRetirar -= 10000
            billetes10000 += 1
        if aux >= substraction+5000:
            substraction += 5000
            montoRetirar -= 5000
            billetes5000 += 1
    print('billetes 20000='+str(billetes20000)+'')
    print('billetes 10000='+str(billetes10000)+ '')
    print('billetes 5000='+str(billetes5000)+'')
    salir = input('¿Salir? ')