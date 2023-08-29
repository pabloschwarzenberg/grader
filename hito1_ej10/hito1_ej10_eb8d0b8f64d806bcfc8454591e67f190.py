#Cajero Automático
cajero=1000000
saldo_cuenta=100000
intentos_clave=0
h=0
while h==0:
    usuario=int(input("ingrese su usuario:"))
    clave=int(input("Ingrese su clave:"))
    if usuario==10334151 and clave==1803:
        print("Ud tiene un saldo en su cuenta de: $",saldo_cuenta,"¿cuánto desea retirar?")
        monto=int(input("ingrese monto deseado:"))
        if monto>saldo_cuenta:
            print("monto no permitido, ingrese otro monto con respecto a su saldo")
        if monto<saldo_cuenta:
            print("espere un momento...")
            print("dinero retirado")
            saldo_cuenta=saldo_cuenta-monto
            cajero=cajero-monto
            print("saldo cuenta=", saldo_cuenta)
            print("saldo cajero=", cajero)
            p=input("Presione N para salir:")
            if p!="N":
                break
    elif usuario==10334151 and clave!=1803:
        print("clave incorrecta")
        intentos_clave=intentos_clave+1
        print("le quedan", 3-intentos_clave, "intentos")
    if intentos_clave==3:
        print ("clave bloqueada")
        break
    