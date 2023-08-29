saldo_cajero=1000000
usuario=int(input('Ingrese su usuario'))
saldo_usuario=100000
intentos_clave = 0
while(intentos_clave<=2):
    if 10334151==usuario:
            clave=input('Ingrese su clave')
            if clave=='1803':
                dinero_a_retirar=int(input('Cuanto va a retirar'))
                if dinero_a_retirar<=saldo_usuario:
                    saldo_usuario=saldo_usuario-dinero_a_retirar
                    saldo_cajero=saldo_cajero-dinero_a_retirar
                    print(saldo_usuario)
                    print(saldo_cajero)
                elif dinero_a_retirar>saldo_usuario:
                    print('monto no permitido')
            else:
                print('clave invalida')
                intentos_clave += 1
    if intentos_clave==3:
        print('tarjeta bloqueada')
        break
