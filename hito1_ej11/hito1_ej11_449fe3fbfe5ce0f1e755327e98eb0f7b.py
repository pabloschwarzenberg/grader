#Cajero Automático
print('Buenos días')
resp = 'N'
while resp=='N':
    saldo_cajero = 1000000
    saldo_cuenta = 100000
    clave_correcta = False
    V = 20
    D = 40
    C = 40
    
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
            monto = int(input("Ingrese monto a retirar: "))
            while monto>100000 or (monto%5000)!=0:
                print('Monto no permitido')
                monto = int(input("Ingrese monto a retirar: $"))
            saldo_cajero = saldo_cajero-monto
            saldo_cuenta = saldo_cuenta-monto
            if monto%20000==0:
                cV = monto//20000
                V = V - cV
                monto = monto - cV*20000
                print('Billetes 20000 =',cV)
            elif monto%10000==0:
                cD = monto//10000
                D = D - cD
                monto = monto - cD*10000
                print('Billetes 10000 =',cD)
            else:
                cC = monto//5000
                C = C - cC
                print('Billetes 5000 =',cC)
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
