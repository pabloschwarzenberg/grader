saldo_c = 1000000
saldo_u = 100000
i = 0
continuar = 'N'

while continuar == 'N':
    usuario = int(input())
    if usuario == 10334151:
        while True:
            clave = int(input())
            i += 1
            if clave == 1803:
                retiro = int(input())
                if retiro > saldo_u:
                    print('monto no permitido')
                else:
                    saldo_u -= retiro
                    saldo_c -= retiro
                    print('saldo cuenta=', saldo_u)
                    print('saldo cajero=', saldo_c)
                    continuar = input()
                    break
            else:
                print('clave invalida')
                if i >= 3:
                    print('tarjeta bloqueada')
                    continuar = 'S'
                    break