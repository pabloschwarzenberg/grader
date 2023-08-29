#Cajero Automático
pic=1000000
piw=100000
ci=0
while ci<3:
    usuario=int(input("Ingrese su usuario:"))
    clave=int(input("Ingrese su clave:"))
    if (usuario!=10334151)or(clave!=1803):
        print("clave invalida")
        ci=ci+1
        if c==3:
                    print("tarjeta bloqueada")
    elif (usuario==10334151)and(clave==1803):
        ci=3
        mar=int(input("Monto a retirar:"))
        if piw-mar<0:
            print("monto no permitido")
        elif piw-mar>=0:
            print("saldo cuenta=", piw-mar)
            print("saldo cajero=", pic-mar)
            
 
