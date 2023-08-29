S_cajero = 1000000
S_cuenta = 100000
intentos = 0

while True:
    usuario = input('Ingrese el número de usuario: ')
    clave = input('Ingrese la clave: ')

    if usuario == '10334151' and clave == '1803':
        print('Inicio de sesión exitoso')
        break
    else:
        print('Clave inválida')
        intentos = intentos + 1

    if intentos == 3:
        print('Tarjeta bloqueada')
        exit()

while True:
    monto = float(input('Ingrese el monto a retirar: '))

    if monto <= S_cuenta:
        if monto <= S_cajero:
            S_cuenta = S_cuenta - monto
            S_cajero = S_cajero - monto
            print('Retiro exitoso')
            print('Saldo cuenta =', S_cuenta)
            print('Saldo cajero =', S_cajero)
        else:
            print('Monto no permitido: saldo insuficiente en el cajero')
    else:
        print('Monto no permitido: saldo insuficiente en la cuenta')

    continuar = input('¿Desea realizar otra operación? (s/n): ')
    if continuar.lower() != 's':
        break
