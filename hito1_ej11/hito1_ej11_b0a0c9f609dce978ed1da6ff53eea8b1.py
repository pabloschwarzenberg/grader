cantidad_billete_veinte_mil = 20
cantidad_billete_diez_mil = 40
cantidad_billete_cinco_mil = 40
billete_cinco_mill = 5000 * cantidad_billete_cinco_mil
billete_diez_mil = 10000 * cantidad_billete_diez_mil
billete_veinte_mil = 20000 * cantidad_billete_veinte_mil
saldo_cajero = billete_cinco_mill + billete_diez_mil + billete_veinte_mil
saldo_usuario = 100000
intento = 0
letra_continuar = 'N'
usuario = input("usuario: ")
clave = input("contraseña: ")
while letra_continuar.upper() == 'N':
    if (clave == '1803' and usuario == '10334151'):
        monto_retiro = int(input("monto de retiro: "))
        if monto_retiro > saldo_usuario or monto_retiro > saldo_cajero:
            print("monto no permitido")
        else:
            if monto_retiro // 20000 > 0 and cantidad_billete_veinte_mil > 0:
                cantidad_billetes = monto_retiro // 20000
                resto = monto_retiro - (20000 * cantidad_billetes)
                cantidad_billete_veinte_mil -= cantidad_billetes
                print("billetes 20000=" + str(cantidad_billetes))
                if resto > 0:
                    if resto // 10000 > 0 and cantidad_billete_diez_mil > 0:
                        cantidad_billetes = resto // 10000
                        resto = resto - (10000 * cantidad_billetes)
                        cantidad_billete_diez_mil -= cantidad_billetes
                        print("billetes 10000=" + str(cantidad_billetes))
                    elif resto // 5000 > 0 and cantidad_billete_cinco_mil > 0:
                        cantidad_billetes = resto // 5000
                        cantidad_billete_cinco_mil -= cantidad_billetes
                        print("billetes 5000=" + str(cantidad_billetes))                
                        saldo_cajero -= monto_retiro
                        saldo_usuario -= monto_retiro
                        arr_print = []
                        arr_print.append('saldo cuenta=' + str(saldo_usuario))
                        arr_print.append('saldo cajero=' + str(saldo_cajero))
                        print(arr_print)
                        letra_continuar = input('para continuar presione la letra "N": ')
    else:
        intento += 1
        if intento >= 3:
            print("tarjeta bloqueada")
            letra_continuar = 'L'
        else:
            print("clave invalida")
            usuario = input("usuario: ")
            clave = input("clave: ")
