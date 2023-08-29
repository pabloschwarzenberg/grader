#cajero automatico
print('Bienvenido al cajero')
numero = 1
u=(100000)
w=(1000000)
e=(0)
f=(0)
while True:
print('Ingrese su usuario')
a=input('usuario: ')
print('--------------')
if a!='10334151':
        print('Inténtelo denuevo1')
        print('-----------------')
    else:
        print('-----------------')
        while numero <= 3:
            print('Ingrese su clave')
            b=input(':')
            if b!='1803':
                print('Inténtelo denuevo2')
                print('-----------------')
                numero = numero + 1
                print('lleva ' +str(numero), 'intentos')
                if numero > 3:
                    print('Tarjeta Bloqueada')
            if b=='1803':
                print('Bienvenido usuario')
                print('Usted tiene 100000 pesos')
                print('Desea retirar dinero?')
                c=input('S/N:')
                if c=='s':
                    print('Inserte la cantidad de dinero que desea retirar')
                    while True:
                        d=(input(':'))
                        e = u+int(d)*-1
                        f = w+int(d)*-1
                        if int(d) < u and int(d) > 0:
                            print('usted retiró ' +str(d)+ 'pesos')
                            print('El cajero tiene ' +str(f)+ 'pesos restantes')
                            print('Su saldo es: ' +str(e)+ 'pesos')
                            print('Debe esperar hasta mañana para poder hacer otra operación')
                            print('Sesión Finalizada')
                            print('------------------')
                        else:
                            print('Monto no permitido, la sesión ha finalizado')
                            print('-------------------')
                        break
                    break
                if c!='s':
                    print('Gracias por su visita')
                    print('---------------------')
                    break
    if numero > 3:
        break