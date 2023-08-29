#Cajero Automático
usuario=int(input("ingrese su usuario: "))
clave=int(input("ingrese su clave: "))
if usuario==10334151 and clave==1803:
    plata=int(input("cuanto desea retirar: "))
    if plata>100000:
        print("monto no permitido")
    else:
        x=100000-plata
        y=1000000-plata
        print("saldo cuenta=",x)
        print("saldo cajero=",y)
else:
    clave=int(input("ingrese su clave: "))
    if usuario==10334151 and clave==1803:
        plata=int(input("cuanto desea retirar: "))
        if plata>100000:
            print("monto no permitido")
        else:
            x=100000-plata
            y=1000000-plata
            print("saldo cuenta=",x)
            print("saldo cajero=",y)
    else:
        clave=int(input("ingrese su clave: "))
        if usuario==10334151 and clave==1803:
             plata=int(input("cuanto desea retirar: "))
             if plata>100000:
                 print("monto no permitido")
             else:
                 x=100000-plata
                 y=1000000-plata
                 print("saldo cuenta=",x)
                 print("saldo cajero=",y)
        else:
            print("tarjeta bloqueada")

