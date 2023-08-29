#Cajero Automático
usuario=int(input("Ingrese número de usuario: "))
if(usuario==10334151):
    intento=0
    while intento<=3:
        clave=int(input("Ingrese su clave de cajero: "))
        if clave==1803:
            retiro=int(input("Ingrese el monto a retirar: "))
            if 0<retiro<=100000:
                saldocajero=1000000-retiro
                saldocuenta=100000-retiro
                print("Saldo Cuenta=",saldocuenta)
                print("Saldocajero=",saldocajero)
                b20=retiro//20000
                r1=retiro%20000
                b10=r1//10000
                r2=r1%10000
                b5=r2//5000
                print("Billetes de 20000=",b20,"  Billetes de 10000=",b10, " Billetes de 5000=",b5)
                break
            else:
                print(" SALDO NO PERMITIDO")
            
        else:
            print("Clave erronea")
            intento=intento+1
    
else:
    print("Usuario invalido")
if(intento>=3):
        print("Tarjeta bloqueada")
    