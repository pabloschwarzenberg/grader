#Cajero Automático
cuenta=eval(input("Ingrese cuenta:"))
clave_cajero=""
intentos=3
saldo_cajero=1000000
saldo_cuenta=100000
retiro=""
por_20=20
por_10=40
por_5=40
if(cuenta==10334151):
    while(clave_cajero==""):
        clave_cajero=eval(input("ingrese su clave por favor:"))
        if(clave_cajero!=1803):
            intentos=intentos-1
            print("clave incorrecta, le quedan", intentos, "intento(s)")
            clave_cajero=""
            if(intentos==0):
                print("tarjeta bloqueada")
                clave_cajero=("tarjeta bloqueada")
        if(clave_cajero==1803):
            while(retiro==""):
                retiro=eval(input("Ingrese monto a retirar:"))
                if(retiro>saldo_cuenta):
                    print("monto no permitido")
                    retiro=""
            if(retiro<saldo_cuenta):
                por_20=retiro//20000
                por_10=(retiro%20000)//10000
                por_5=((retiro%20000)%10000)//5000
                print("saldo cuenta=", saldo_cuenta-retiro)
                print("saldo cajero=", saldo_cajero-retiro)
                print("billetes 20000=", por_20)
                print("billetes 10000=", por_10)
                print("billetes 5000=", por_5)
                
    if(clave_cajero=="tarjeta bloqueada"):
        print()