'''Tu cajero debe pedir un usuario y una clave para ingresar. Al principio debe tener 1.000.000 como saldo inicial. 
Tu cajero debe dejar ingresar al usuario 10334151 con la clave 1803, quien tiene al inicio del programa 100.000 en su cuenta. 
Lo único que se puede hacer en este nivel es retirar dinero de la cuenta corriente. Tu programa debe validar la clave y el monto a retirar, 
indicando el mensaje “clave invalida” cuando la clave no corresponde y al tercer intento fallido debe indicar “tarjeta bloqueada” y salir del programa. 
Si la clave es válida, debe preguntar por el monto a retirar. Cuando se hace el retiro de un monto que no es válido debe indicar “monto no permitido”, 
si el monto se puede retirar debe actualizar los saldos e imprimir el nuevo saldo que quedó en la cuenta corriente y el cajero, por ejemplo al retirar 45.000 debiera imprimir:

saldo cuenta=55000
saldo cajero=955000

Tu programa debe repetirse continuamente, para salir la persona debe ingresar algo distinto a la letra “N”.'''

usuario = 0
clave = 0
Attempts = 0
Saldo = 1000000
SaldoCorriente = 100000
MontoRetiro = 0

while usuario != 10334151:
    usuario = int(input('Usuario: '))
    print(usuario)
        

while clave != 1803:
    clave = int(input('Clave:'))
    if clave != 1803:
        print('Clave incorrecta')
        Attempts += 1
        if Attempts >= 3:
            print('Tarjeta Bloqueada')
            break
        
while True:
    MontoRetiro = input('Monto a retirar: ')
    numberFlag = MontoRetiro.isnumeric()
    if numberFlag == True:
        if int(MontoRetiro) <= Saldo and int(MontoRetiro) >= 0:
           Saldo -= int(MontoRetiro)
           SaldoCorriente -= int(MontoRetiro)
           print('saldo cuenta=', SaldoCorriente)
           print('saldo cajero=',Saldo)
           numberFlag == False
        elif int(MontoRetiro) > Saldo:
             print('Monto no permitido.')
             numberFlag == False
    elif MontoRetiro != 'N':
        break
        
        
    
        
        
        
        
        
        
        
        
        
'''
while MontoRetiro != 'N':
    MontoRetiro = input('Monto a retirar: ')
    if MontoRetiro:
    
    
    if int(MontoRetiro) <= Saldo and int(MontoRetiro) >= 0:
        Saldo =- int(MontoRetiro)
        SaldoCorriente =+ int(MontoRetiro)
        print('saldo cuenta=', SaldoCorriente)
        print('saldo cajero=',Saldo)
    elif int(MontoRetiro) > Saldo:
        print('Monto no permitido.')
'''

