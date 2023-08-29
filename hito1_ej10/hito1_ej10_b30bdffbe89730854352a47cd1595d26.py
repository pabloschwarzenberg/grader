#Cajero Automático
salir=False
saldoCuenta=100000
saldoCajero=1000000
while(salir==False):   
    password="1803"   
    for i in range(4):
        if i>0:
            print("clave inválida")
        if(i>2):
            print("tarjeta bloqueada")
            salir=True
            break
        clave=input("Clave: ")
        if clave=="N":
            salir=True  
        if clave==password:
            while(True):
                monto=int(input("indique el monto a retirar: "))
                if monto<saldoCuenta:
                    saldoCuenta=saldoCuenta-monto
                    saldoCajero=saldoCajero-monto
                    print("saldo cuenta=",saldoCuenta)
                    print("saldo cajero=",saldoCajero)
                    break
                else:
                    print("monto no permitido")
    
     