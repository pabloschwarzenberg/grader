passw = False
clave = True
monto_i = False
Usuario = False
finish = False
saldo_cuenta = 100000
saldo_cajero = 1000000
saldo_actualizado_cu = saldo_cuenta
saldo_actualizado_ca = saldo_cajero
usuario = "N"
claveU = "N"
monto_i = "N"
variable = "abcdefghijklmñopqrstuvwxyzABCDEFGHIJKLMÑOPQRSTUVWXYZ"
billetes_20 = 20
billetes_10 = 40
billetes_5 = 40



                
    
    

while clave == True and usuario not in variable and claveU not in variable and monto_i not in variable: 
    while Usuario == False:
        usuario = input("Ingrese usuario: ")
        if usuario == "10334151":
            Usuario = True
    intento = 0
    while passw == False:
        claveU = input("ingrese clave: ")
        if claveU != "1803":
            print("clave invalida")
            intento += 1
            if intento == 3:
                print("tarjeta bloqueada")
                clave = False
                break

        if intento == 3:
            break
                
        if claveU == "1803":
            passw = True
    
    while passw == True:
        monto_i = input("ingrese monto:")
        
        if monto_i not in variable:
            if int(monto_i) > saldo_actualizado_cu or int(monto_i) > saldo_actualizado_ca:
                print("monto no permitido")
            else:
                nuevo_saldo_cuenta = saldo_actualizado_cu - int(monto_i)
                nuevo_saldo_cajero = saldo_actualizado_ca - int(monto_i)
                saldo_actualizado_cu = nuevo_saldo_cuenta
                saldo_actualizado_ca = nuevo_saldo_cajero

                billetes20 = ""
                billetes10 = ""
                billetes5 = ""

                if int(monto_i) > 20000:
                    billetes20 = int(monto_i)//20000
                    
                        
                    a = int(monto_i) - billetes20*20000
                    
                        
                    if a >= 10000:
                        billetes10 = 1
                        b = a - 10000
                        if b == 5000:
                            billetes5 = 1
                        else:
                            billetes = 0
                    elif a == 5000:
                        billetes5 = 1
                        billetes10 = 0
                    else:
                        billetes5 = 0
                        billetes10 = 0
                elif int(monto_i) >= 10000:
                    billetes10 = 1
                    c = monto_i - billetes10*10000
                    if c == 5000:
                        billetes5 = 1
                        

                elif int(monto_i) == 5000:
                    billetes5 = 1


    

                print("saldo cuenta=" + str(saldo_actualizado_cu))
                print("saldo cajero=" + str(saldo_actualizado_ca))
                print("billetes 20000=" + str(billetes20))
                print("billetes 10000=" + str(billetes10))
                print("billetes 5000=" + str(billetes5))

        else:
            break
    if monto_i in variable:
        break


        
