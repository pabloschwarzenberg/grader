s_caj=1000000
saldo=100000
exit_prog=False
while True:
    sesion=False
    error=0
    print('Bienvenido al cajero automático')
    print('saldo del cajero: $',s_caj)
    while sesion==False:
        usuario=input('Nombre de usuario: ')
        clave=input('Clave: ')
        if usuario!='10334151' or clave!='1803':
            print('Nombre de usuario o clave inválidos')
            error=error+1
            print(3-error,' intentos restantes')
            if error==3:
                print('Se han detectado tres errores consecutivos, su tarjeta ha sido bloqueada')
                exit_prog=True
                break
        else:
            print('Bienvenido de nuevo usuario',usuario)
            sesion=True
    if exit_prog==True:
        break
    while sesion==True:
        retiro=False
        while retiro==False:
            print('Saldo de su tarjeta: $',saldo)
            monto=int(input('Monto que desea girar: '))
            if monto>saldo:
                print('No tiene suficiente saldo en su tarjeta')
            elif monto<=0:
                print('Por favor ingrese un monto válido')
            else:
                saldo=saldo-monto
                s_caj=s_caj-monto
                print('Giro exitoso')
                print('Saldo actual: $',saldo)
                print('Saldo del cajero: $',s_caj)
                retiro=True
        cerrar_s=input('Desea cerrar la sesión?(S/N): ')
        if cerrar_s=='S':
            print('Gracas por operar con nosotros')
            break
    if exit_prog==True or cerrar_s=='S':
        break