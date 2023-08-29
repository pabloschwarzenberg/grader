usuario=int(input("ingrese su usuario"))
clave=int(input("ingrese su clave"))
saldo = 100000
cajero= 1000000
intentos = 1
while intentos !=3:
    if usuario ==10334151 and clave==1803:
        giro=int(input("ingrese el monto que desea girar"))
        saldo = saldo - giro
        cajero = cajero - giro
        if giro>saldo:
            print("monto no permitido")
            continuar=input(" si desea continuar presione N")
            if continuar=="N":
                pass
            else:
                break
    if giro<=saldo:
        print("saldo cuenta=",saldo)
        print("saldo cajero=",cajero)
        continuar=str(input(" si desea continuar presione n"))
    

        
if usuario!= 10334151 or clave!=1803:
    while intentos !=3:
        intentos = intentos+1
        print("clave invalida, vuelvo a intentarlo")
        usuario=int(input("ingrese su usuario"))
        clave=int(input("ingrese su clave"))
        if intentos ==3:
            print("tarjeta bloqueada")
            break