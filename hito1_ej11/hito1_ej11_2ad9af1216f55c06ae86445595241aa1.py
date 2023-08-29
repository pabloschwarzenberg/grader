#cajero automatico nivel 2

def billetes_entregar(monto,b20,b10,b5):
    entregar20=0
    entregar10=0
    entregar5=0
    monto_solicitado=monto
    while monto>0:
        solicitado=monto
        if monto%20000==0 and b20>0 and monto>0:
            b20-=1
            entregar20+=1
            monto-=20000
        if monto%10000==0 and b10>0 and monto>0:
            b10-=1
            entregar10+=1
            monto-=10000       
        if monto%5000==0 and b5>0 and monto>0:
            b5-=1
            entregar5+=1
            monto-=5000 
        if monto==solicitado:
            break
    if entregar20*20000+entregar10*10000+entregar5*5000!=monto_solicitado:
        entregar20=0
        entregar10=0
        entregar5=0
    return entregar20,entregar10,entregar5

user=input("Ingrese usuario: ")
password=input("ingrese clave: ")
intento=0
while user !="10334151" or password!="1803":
    intento=intento+1
    if intento==3:
        print("tarjeta bloqueada")
        break
    print("clave invalida")
    user=input("Ingrese usuario: ")
    password=input("ingrese clave: ")
if intento<3:
    saldoCajero=1000000
    saldoCliente=100000
    b20=20
    b10=40
    b5=40

    cont="N"
    while cont =="N":
        retiro=input("¿Cuánto desea retirar?:")
        if retiro.isdigit()==True:
            retiro=int(retiro)
            if retiro<=saldoCliente and retiro<=saldoCajero and retiro>0 and retiro%5000==0:

                billetes=billetes_entregar(retiro,b20,b10,b5)
                if billetes==(0,0,0):
                    print("monto no permitido")
                else:  
                    saldoCajero-=retiro
                    saldoCliente-=retiro
                    entregar20=billetes[0]
                    entregar10=billetes[1]
                    entregar5=billetes[2]
                    b20=b20-entregar20
                    b10=b10-entregar10
                    b5=b5-entregar5
                    print("billetes 20000="+str(entregar20))
                    print("billetes 10000="+str(entregar10))
                    print("billetes 5000="+str(entregar5))
                    print("saldo cuenta="+str(saldoCliente))
                    print("saldo cajero="+str(saldoCajero))
                    
            else:
                print("monto no permitido") 
        else:
            print("monto no permitido")
        cont=input("N para continuar")
