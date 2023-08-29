import sys
saldocajero=int(1000000)
saldocuenta=int(100000)
contadorclave=0
while contadorclave<3:
    usuario=int(input("Usuario:"))
    clave=int(input("Clave:"))
    if usuario==10334151 and clave==1803:
        monto=int(input("Monto:"))
        if monto>saldocuenta:
            print("monto no permitido")
        else:
            saldocuenta=saldocuenta-monto
            saldocajero=saldocajero-monto
            print("saldo cuenta=",saldocuenta)
            print("saldo cajero=",saldocajero)
            salir = input("para salir ingrese cualquier letra diferente de N")
            if salir != "N":
                sys.exit()
                
            
            
    elif clave!=1803 or usuario!=10334151:
        print("Clave o usuario invalido")
        contadorclave += 1
        if contadorclave == 3:
            print("tarjeta bloqueada")
            salir = input("para salir ingrese cualquier letra diferente de N")
            if salir != "N":
                sys.exit()


            


    

