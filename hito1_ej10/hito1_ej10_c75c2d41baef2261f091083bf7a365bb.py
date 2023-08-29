#Cajero Automático
salir="no"
saldo_cuenta=100000
saldo_cajero=1000000
while salir=="no":
    intentos=3
    while intentos>0:
        usuario=input('introduzca usuario: ')
        clave=input('introduzca clave: ')
        if(usuario== '10334151'  and clave== '1803'):
            print('Bienvenido')
            continuar= True
            while(continuar):
                monto_retiro= int(input("ingrese monto a retirar: "))
                if( saldo_cajero>0 and saldo_cuenta>0):
                    if(saldo_cuenta>monto_retiro):
                        saldo_cuenta= saldo_cuenta- monto_retiro
                        saldo_cajero= saldo_cajero- monto_retiro
                        print('Transacción realizada con exito')
                        print('Saldo cuenta= ',saldo_cuenta)
                        print('Saldo cajero= ',saldo_cajero)
                        continuar=False
                    elif(saldo_cuenta==monto_retiro):
                        saldo_cuenta= saldo_cuenta- monto_retiro
                        saldo_cajero= saldo_cuenta- monto_retiro
                        print('Transacción realizada con exito')
                        print('Su saldo actual es: ',saldo_cuenta)
                        continuar=False
                    else:
                        print("Saldo Insuficiente")
                else:
                    print("Reintentar otro monto")
            break
        else:
            print ('clave o usuario incorrecto')
            intentos=intentos -1
            print ('numero de intentos',intentos)
    if intentos==0:
        print ('usuario bloqueado')
        break
    else:
        salir=input("Deseas salir?")


