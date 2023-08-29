#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
while True:
    cosa = True
    usuario = input()
    if usuario == '10334151':
        verda = False
        for i in range(3):
            clave = input()
            if clave == '1803':
                verda = True
                break
        if not verda:
            print('tarjeta bloqueada')
            break
            cosa = False
        else:
            monto = int(input())
            if monto > saldo_cuenta or monto < 0:
                print('monto no permitido')
            else:
                saldo_cuenta -= monto
                saldo_cajero -= monto
                print('saldo cuenta=' + str(saldo_cuenta))
                print('saldo cajero=' + str(saldo_cajero))
    if not verda:
        print('tarjeta bloqueada')
        break
        cosa = False