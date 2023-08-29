# Cajero Automático
saldo_cajero = 10 ** 6
saldo_cuenta = 10 ** 5

cinco_mil = 40
dies_mil = 40
veite_mil = 20

usuario = int(input())
clave = int(input())

intentos = 3

while usuario != 10334151 and clave != 1803 and intentos != 0:
    print('clave invalida')
    intentos -= 1
    usuario = int(input())
    clave = int(input())

    if intentos == 0:
        print('tarjeta bloqueda')
        break

while intentos != 0:
    monto = input()
    # print('intentos', intentos, monto == 'N')

    if not monto.isnumeric() and monto != 'N':
        intentos = 0


    elif int(monto) > saldo_cuenta:
        print('monto no permitido')
        # monto = input()

    else:
        monto = int(monto)

        saldo_cuenta -= int(monto)
        saldo_cajero -= int(monto)
        print('''saldo cuenta={}
saldo cajero={}'''.format(saldo_cuenta, saldo_cajero))

        veite = monto // 20000

        if veite > veite_mil:
            veite = veite_mil

        veite_mil -= veite
        monto -= 20000 * veite
        print('billetes 20000={}'.format(veite))

        dies = monto // 10000

        if dies > dies_mil:
            dies = dies_mil

        dies_mil -= dies
        monto -= 10000 * dies
        print('billetes 10000={}'.format(dies))

        cinco = monto // 5000
        print('billetes 5000={}'.format(cinco))


