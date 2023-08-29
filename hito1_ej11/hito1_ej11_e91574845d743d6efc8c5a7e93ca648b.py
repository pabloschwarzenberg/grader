billetesdeveinte=20
billetesdediez=40
billetesdecinco=40
pic=billetesdeveinte*20000+billetesdediez*10000+billetesdecinco*5000
piw=100000
ci=0
while ci<3:
    usuario=int(input("Ingrese su usuario:"))
    clave=int(input("Ingrese su clave:"))
    if (usuario!=10334151)or(clave!=1803):
        print("clave invalida")
        ci=ci+1
        if ci==3:
                    print("tarjeta bloqueada")
    elif (usuario==10334151)and(clave==1803):
        ci=3
        mar=int(input("Monto a retirar:"))
        if piw-mar<0:
            print("monto no permitido")
        elif piw-mar>=0:
            vdv=mar//20000
            vdd=(mar-(mar//20000)*20000)//10000
            vdc=(mar-vdv*20000-vdd*10000)//5000
            print("Saldo cajero=", pic-mar)
            print("Saldo cuenta=", piw-mar)
            print("Billetes 20000=",vdv)
            print("Billetes 10000=",vdd)
            print("Billetes 5000=",vdc)
           