#Cajero Automático
p = 1
while p != 0:
    usuario = int(input('Ingresar usuario: '))

    saldo_cajero = 1000000
    saldo_cuenta = 100000
    b = 0
    if usuario == 10334151:
        
        incorrecto = 0
        while incorrecto != 3:
            clave = int(input('Ingresar clave: '))

            if clave == 1803:
                a = 1
                while a != 0:
                    monto_retiro = eval(input('Monto a retirar: '))

                    if monto_retiro > saldo_cajero:
                        print('monto no permitido')
                    else:
                        saldo_cajero = (saldo_cajero-monto_retiro)
                        saldo_cuenta = (saldo_cuenta+monto_retiro)
                        print('saldo cuenta=',saldo_cuenta)
                        print('saldo cajero=',saldo_cajero)

                        pregunta = input('Continuar(c) o salir(s): ')
                        if pregunta == 'c':
                            continue
                        elif pregunta == 's':
                           print('a salido')
                           incorrecto =3
                           break 
                            
                        
                        incorrecto = 3
            elif clave != 1803:
                print('clave invalida')
                incorrecto += 1
                continue
        if pregunta == 's':
            break
        elif incorrecto == 3 and b == 0:
            print('tarjeta bloqueada')
            break
        
        
    else:
        print('usuario no registrado')
        continue
