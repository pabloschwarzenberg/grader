#Cajero Automático
usu = 10334151
clave = 1803
 
usuint = int(input('Ingrese usuario: '))
if usu == usuint:
    inte = 1
    while inte <= 3:
        claveint = int(input('Ingrese contraseña: '))
        if clave == claveint:
            l = True
            break
        elif clave != claveint:
            print('Clave invalida')
            print('Reingrese la clave')
            inte = inte + 1
    if inte == 3:
        print('Tajeta bloqueada')
        exit()
elif usu != usuint:
    print('Usuario invalido')
     
saldo_c = 1000000
saldo_u = 100000

if clave == claveint:
    mo = int(input('Monto a retirar :'))
    if mo > saldo_u:
        print('Monto no permitido')
    elif mo <= saldo_u:
        saldo_c = saldo_c - mo
        saldo_u = saldo_u - mo
        print('saldo cajero =',saldo_c)
        print('saldo cuenta =',saldo_u)




