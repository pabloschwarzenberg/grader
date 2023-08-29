#Cajero Automático
Saldo=1000000
Cuenta=100000
Usuario_p=10334151
Contrasena_p=1803

Intentos=1
Monto=0
Usuario=0
Contrasena=0
Estado='libre'
Ingreso='Cerrado'

while Ingreso!='Valido':

    Usuario=int(input('Ingrese el usuario\n'))
    Contrasena=int(input('Ingrese la contraseña acorde al usuario\n'))

    if Intentos==3:
        print('Tarjeta bloqueada\n')
        Estado='Bloqueado'
        break

    if (Usuario!=Usuario_p)or(Contrasena!=Contrasena_p):
        Intentos=Intentos+1
        print('Clave invalida\n')
    
    else:
        while Ingreso!='Valido':
            Monto=int(input('Ingrese el monto que desea retirar\n'))
            if Monto<=Cuenta:
                Ingreso='Valido'
            else:
                print('Monto no permitido')

Saldo=Saldo-Monto
Cuenta=Cuenta-Monto

if Estado=='libre':
    print('saldo cuenta=',Cuenta,)
    print('saldo cajero=',Saldo)