#Cajero Automático
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
            saldo_retirar = int(input('monto a retirar: '))   # <-----------------
            Cifra1 = saldo_retirar%10
            Cifra2 = (saldo_retirar%100)//10
            Cifra3 = (saldo_retirar%1000)//100
            Cifra4 = (saldo_retirar%10000)//1000
            Cifra5 = (saldo_retirar%100000)//10000
            Cifra6 = (saldo_retirar%1000000)//100000           
            if saldo_retirar > saldo_usuario:
                print('monto no permitido')               
            if saldo_retirar <= saldo_usuario:
                if  100000 <= saldo_retirar <= 999999:
                    Cantidad1 = (int(Cifra6)*100000)    
                    if Cantidad1 == 100000:
                        CantBilletes20k = Cantidad1//20000
                        CantBilletes10k = 0
                        CantBilletes5k = 0
                if  10000 <= saldo_retirar <= 99999:
                    Cantidad2 = (int(Cifra5)*10000)
                    if Cifra5 != 0:
                        if Cifra5 % 2 == 0:
                            CantBilletes20k = Cifra5//2
                            Cantidad2 = (int(Cifra5)*10000)
                            CantBilletes10k = 0
                        if Cifra5 % 2 != 0:        
                            CantBilletes10k = Cifra5
                            Cantidad2 = (int(Cifra5)*10000)
                            CantBilletes20k = 0
                    if Cifra5 == 0:
                        CantBilletes20k = 0
                        CantBilletes10k = 0                        
                    if Cifra4 != 0:
                        Cantidad3 = (int(Cifra4)*1000)
                        CantBilletes5k = Cantidad3//Cantidad3
                    if Cifra4 == 0:
                        CantBilletes5k = 0                       
                if  1000 <= saldo_retirar <= 9999:
                    if Cifra4 != 0:
                        Cantidad3 = (int(Cifra4)*1000)
                        CantBilletes5k = Cantidad3//Cantidad3
                        CantBilletes10k = 0
                        CantBilletes20k = 0
                    if Cifra4 == 0:
                        CantBilletes5k = 0                                
                saldo_usuario = saldo_usuario - saldo_retirar
                saldo_cajero = saldo_cajero - saldo_retirar                
                print(str('saldo cuenta=' + str(saldo_usuario)))
                print(str('saldo cajero=' + str(saldo_cajero)))
                print(str('billetes 20000=')+str(CantBilletes20k))
                print(str('billetes 10000=')+str(CantBilletes10k))
                print(str('billetes 5000=')+str(CantBilletes5k))               
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