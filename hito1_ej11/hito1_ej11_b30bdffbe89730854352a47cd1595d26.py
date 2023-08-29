#Cajero Automático
salir=False
saldoCuenta=100000
saldoCajero=1000000
b20=20
b10=40
b5=40
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
                    b20g=monto//20000
                    monto=monto%20000
                    b10g=monto//10000
                    monto=monto%10000
                    b5g=monto//5000
                    b20=b20-b20g
                    b10=b10-b10g
                    b5=b5-b5g
                    print("billetes 20000=",b20g)
                    print("billetes 10000=",b10g)
                    print("billetes 5000=",b5g)
                    
                    break
                else:
                    print("monto no permitido")
    