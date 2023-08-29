u=int(input("ingrese su usuario"))
c= 1803
vegan=0
sc=0
sca=0
while(vegan<3):
    si= 1000000
    s=100000 
    z=int(input("ingrese su clave"))
    if(c==z):
        print("")

        montoart=int(input("ingrese monto de retiro"))
        if(montoart<s and montoart<si):
            print()
        elif(montoart>s and montoart>si):
            print("monto no permitido")
        sc=100000-montoart
        sca=1000000-montoart
        sc=str(sc)
        sca=str(sca)
        print("saldo cuenta="+sc)
        print("saldo cajero="+sca) 
        vegan=vegan+4
    else:
        vegan=vegan+1

if(vegan==3):
        print("tarjeta bloqueada")
