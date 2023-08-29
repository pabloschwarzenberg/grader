#cajero automatico nivel 1
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
    retiro=0
    cont="N"
    while cont =="N":
        retiro=input("monto a retirar: ")
        if retiro!="N":
            if retiro.isdigit()==True:
                retiro=int(retiro)
                if retiro<=saldoCliente and retiro<=saldoCajero and retiro>0:
                    saldoCajero-=retiro
                    saldoCliente-=retiro
                    print("saldo cuenta="+str(saldoCliente))
                    print("saldo cajero="+str(saldoCajero))
                else:
                    print("monto no permitido") 
            else:
                print("monto no permitido")
        cont=input("N para continuar")