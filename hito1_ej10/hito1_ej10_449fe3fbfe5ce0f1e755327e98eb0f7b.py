#Cajero Automático
print('Buenos días')
resp = 'N'
while resp=='N':
    saldo_cajero = 1000000
    saldo_cuenta = 100000
    clave_correcta = False

    usuario = input('Ingrese su usuario: ')

    while usuario!='10334151':
        print('Usuario inválido')
        usuario = input('Ingrese su usuario: ')
            
    for i in range(3):
        clave=input('Ingrese su clave: ')
        if clave=='1803':
            clave_correcta = True
            print("Saldo del cajero: $",saldo_cajero)
            print('Saldo de la cuenta corriente: $',saldo_cuenta)
            monto = int(input("Ingrese monto a retirar: $"))
            while monto>100000:
                print('Monto no permitido')
                monto = int(input("Ingrese monto a retirar: $"))
                
            saldo_cajero = saldo_cajero-monto
            saldo_cuenta = saldo_cuenta-monto
            print('saldo cuenta =',saldo_cuenta)
            print('saldo cajero =',saldo_cajero)
            break
        else:
            print("clave inválida")
    if not clave_correcta:
        print('Tarjeta bloqueada')
    print('Si desea realizar otra trasacción presione N, si desea salir pulse cualquier otro caracter')
    resp = input()

print('Adiós, que tenga un buen día')
