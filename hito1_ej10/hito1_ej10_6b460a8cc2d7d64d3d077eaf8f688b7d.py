


cajero_balance_inicial = 1000000
usuario_balance_inicial = 100000

usuario_guard =10334151
clave_guard = 1803
verificacion = False
intentos = 1
bucle = True


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
        usuario_balance = usuario_balance-monto_activo
        cajero_balance = cajero_balance-monto_activo
#         print('Ha retirado: ${:,.0f} '.format(monto_activo))
#         print('Balance Nuevo Usuario: ${:,.0f} '.format(usuario_balance))
#         print('Balance Nuevo Cajero: ${:,.0f}'.format(cajero_balance))
        print("['saldo cuenta="+str(usuario_balance)+"','saldo cajero="+str(cajero_balance)+"']")
        
    else:
        print('Monto No Valido. Balance cajero = ${:,.0f}'.format(cajero_balance),'  y Balance Usuario = ${:,.0f}'.format(usuario_balance))
    cont_check = input('Pulse "N" para continuar, cualquier otra letra para detener el programa')
    if cont_check.lower() == letra_continuar:
        continue
        
    elif cont_check.lower() != letra_continuar:
        verificacion=False
    
    
     