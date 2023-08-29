
cajero_balance_inicial = 1000000
usuario_balance_inicial = 100000

usuario_guard =10334151
clave_guard = 1803
verificacion = False
intentos = 1
bucle = True
billetes_inicial = {'20000':40,'10000':40,'5000':40}

while bucle:
    
    usuario_activo = int(input('Introducir Codigo Usuario: '))
    pin_activo = int(input('Introducir PIN Secreto: '))
    
    if usuario_activo == usuario_guard and pin_activo == clave_guard:
        verificacion = True
        print('Usuario: ',usuario_activo,' Verificado')
        bucle = False
    else:
        
        if intentos == 3:
            print('TARJETA BLOQUEADA')
            bucle = False
        
        else: 
            print('PIN INCORRECTO')
            intentos +=1

letra_continuar = 'n'
cajero_balance,usuario_balance = cajero_balance_inicial,usuario_balance_inicial
while verificacion == True:
     
    monto_activo = int(input('Indique monto a retirar:'))
    if monto_activo <= usuario_balance and monto_activo <=cajero_balance:
        
        cantidad_entregar = monto_activo
        


        usuario_balance = usuario_balance-monto_activo
        cajero_balance = cajero_balance-monto_activo
        print("['saldo cuenta="+str(usuario_balance)+"','saldo cajero="+str(cajero_balance)+"']")
        
        if billetes_inicial['20000'] >0:
            cantidad_20mil = cantidad_entregar//20000
            if cantidad_20mil <= billetes_inicial['20000']:
                billetes_inicial['20000'] = billetes_inicial['20000']-cantidad_20mil
                cantidad_entregar = cantidad_entregar%20000
                print('billetes 20000='+str((cantidad_20mil)))
        if billetes_inicial['10000'] >0:
            cantidad_10mil = cantidad_entregar//10000
            if cantidad_10mil <= billetes_inicial['10000']:
                billetes_inicial['10000'] = billetes_inicial['10000']-cantidad_10mil
                cantidad_entregar = cantidad_entregar%10000
                print('billetes 10000='+str(cantidad_10mil))
        if billetes_inicial['5000'] >0:
            cantidad_5mil = cantidad_entregar//5000
            if cantidad_5mil <= billetes_inicial['5000']:
                billetes_inicial['5000'] = billetes_inicial['5000']-cantidad_5mil
                cantidad_entregar = cantidad_entregar%5000
                print('billetes 5000='+str(cantidad_5mil))     
    else:
        print('Monto No Valido. Balance cajero = ${:,.0f}'.format(cajero_balance),'  y Balance Usuario = ${:,.0f}'.format(usuario_balance))
    cont_check = input('Pulse "N" para continuar, cualquier otra letra para detener el programa')
    if cont_check.lower() == letra_continuar:
        continue
        
    elif cont_check.lower() != letra_continuar:
        verificacion=False
    
    
