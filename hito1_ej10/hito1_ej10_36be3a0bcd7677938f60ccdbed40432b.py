#Cajero Automático
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


    

                print("saldo cuenta=" + str(saldo_actualizado_cu))
                print("saldo cajero=" + str(saldo_actualizado_ca))

        else:
            break
    if monto_i in variable:
        break


        