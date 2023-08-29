saldo_cajero = 1000000
saldo_usuario = 100000
intentos = 0

while intentos < 3:    
    datos = input('ingresa datos: ')
    datos2 = datos.replace(" ", "")
    if datos2.isdigit() == True:
        datos3 = int(datos2)
        usuario = datos3//10000
        clave = datos3%10000    
        if clave == 1803:            
            saldo_retirar = int(input('monto a retirar: '))               
            if saldo_retirar > saldo_usuario:
                print('monto no permitido')                
            if saldo_retirar <= saldo_usuario:
                saldo_usuario = saldo_usuario - saldo_retirar
                saldo_cajero = saldo_cajero - saldo_retirar
                print(str('saldo cuenta=' + str(saldo_usuario)))
                print(str('saldo cajero=' + str(saldo_cajero)))
        if clave != 1803:
            print('clave invalida')
            intentos += 1
        if intentos == 3:
            print('tarjeta bloqueada')
            break                
    if datos2.isalpha() == True:
        if datos2 != 'N':
            break
        if datos2 == 'N':
            intentos = 0