#Cajero Automático
salir="N"
saldoCuenta=100000
saldoCajero=1000000
validado="N"
intento=3



while validado=="N" and intento>0:
    Usuario =  int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese clave: "))

    if Usuario==10334151 and clave==1803:
       validado="V"
    else:
        print("clave invalida")

    intento -= 1



while salir=="N" and validado=="V":

    monto =  int(input("Que monto desea retirar? $:"))
    if saldoCuenta<monto:
        print("monto no permitido")
    else:
       saldoCuenta -= monto
       saldoCajero -= monto

    print("saldo cuenta="+str(saldoCuenta))
    print("saldo cajero="+str(saldoCajero))
    salir =  str(input("Desea Salir (S/N): ")).upper()
    

if intento==0:
    print("tarjeta bloqueada")
      