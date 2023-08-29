#Cajero Automático
saldo_c = 1000000
saldo_u = 100000
b20 = 20
b10 = 40
b05 = 40


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
                    r20 = retiro//20000
                    r10 = (retiro - r20*20000)//10000
                    r05 = (retiro - r20*20000 - r10*10000)//5000
                    print('saldo cuenta=', saldo_u)
                    print('saldo cajero=', saldo_c)
                    print('billetes 20000=', r20)
                    print('billetes 10000=', r10)
                    print('billetes 5000=', r05)
                    continuar = input()
                    break
            else:
                print('clave invalida')
                if i >= 3:
                    print('tarjeta bloqueada')
                    continuar = 'S'
                    break
      