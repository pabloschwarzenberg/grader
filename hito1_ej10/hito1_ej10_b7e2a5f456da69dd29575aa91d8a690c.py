#Cajero Automático
#Tu cajero debe pedir un usuario y una clave para ingresar.
usuario = int(input('Ingresar usuario: '))
clave = int(input('Ingresar clave: '))
#Al principio debe tener 1.000.000 como saldo inicial.
saldo_ic = 1000000          #saldo_inicial_cajero
#Tu cajero debe dejar ingresar al usuario 10334151 con la clave 1803
#quien tiene al inicio del programa 100.000 en su cuenta
saldo_iu = 100000           #saldo_inicial_usuario
#Tu programa debe validar la clave y el monto a retirar
#indicando el mensaje “clave invalida” cuando la clave no corresponde
if clave != 1803:
 print('Clave inválida')
 cont = 0
 while cont <= 3:
     print('Ingrese clave nuevamente')
     clave = int(input('Ingresar clave: '))
     cont += 1
     if cont == 3:     #al tercer intento fallido debe indicar “tarjeta bloqueada” y salir del programa.
         break
 print('Tarjeta bloqueada')
if clave == 1803:
    monto = int(input('¿Cuál es el monto a retirar?: '))
    while monto > saldo_iu:
        print('Monto no permitido->', 'Ingrese monto nuevamente')
        monto = int(input('¿Cuál es el monto a retirar?: '))
saldo_fcta = saldo_iu - monto  # saldo final cta crrte
saldo_fcjr = saldo_ic - monto  # saldo final cajero
print('Saldo cuenta=',saldo_fcta, 'Saldo cajero=',saldo_fcjr)
