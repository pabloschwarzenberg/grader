#Cajero Automático
print('** CAJERO AUTOMÁTICO NIVEL 2** ')

cont = 0
saldo_cajero = 1000000
saldo_cuenta = 100000
n_20 = 20
n_10 = 40
n_5 = 40
while cont < 3:
    print('-- Saldo cajero: '+str(saldo_cajero)+' --')
    print('20000: '+str(n_20))
    print('10000: '+str(n_10))
    print('5000: '+str(n_5))
    usuario = int(input('Ingrese número de usuario: '))
    clave = int(input('Ingrese clave: '))

    if usuario == 10334151:
        if (clave != 1803):
            print('clave invalida')
            cont = cont + 1

        else:
            print('-- Saldo cuenta: '+str(saldo_cuenta)+' --')
            monto = int(input('-- Cuanto es el monto deseado a retirar: '))
            if (monto > saldo_cajero) or (monto > saldo_cuenta):
                print('monto no permitido') #no pongo nada para que pregunte denuevo y continue el ciclo

            else: #asumimos que el monto ingresado es multiplo de 5000
                if (monto%5000 == 0):
                    saldo_cajero = saldo_cajero - monto
                    saldo_cuenta = saldo_cuenta - monto
                    print('saldo cuenta='+str(saldo_cuenta))
                    print('saldo cajero='+str(saldo_cajero))

                    a = 0
                    while a < n_20:
                        if monto < 20000:
                            break
                        else:
                            monto = monto - 20000
                            a = a + 1
                    b = 0
                    while b < n_10:
                        if monto < 10000:
                            break
                        else:
                            monto = monto - 10000
                            b = b + 1
                    c = 0
                    while c < n_5:
                        if monto < 5000:
                            break
                        else:
                            monto = monto - 5000
                            c = c + 1

                    if a != 0:
                        print('billetes 20000='+str(a))
                    if b != 0:
                        print('billets 10000='+str(b))
                    if c != 0:
                        print('billetes 5000='+str(c))

                    n_20 = n_20-a
                    n_10 = n_10-b
                    n_5 = n_5-c

                
                    letra = input('Si ingresas la letra N sigues en el programa: ')
                    if letra != 'N':
                        break
                          
    else:
        continue
        
            
if cont == 3:
    print('tarjeta bloqueada')