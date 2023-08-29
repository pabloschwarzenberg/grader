#Cajero Automático
saldoinicialcajero=1000000
cuentausuario=100000
intentos=0
salir=False
clavevalida=False
tarjeta=""

carga_de_5=40
carga_de_10=40
carga_de_20=20

while clavevalida==False:
    usuario=int(input("ingrese nombre de usuario: "))
    clave=int(input("ingrese clave: "))
    monto=int(input("monto a retirar: "))
    repetir=input("")
    if repetir=="n" or repetir=="N":
        salir=True
        break
    if usuario==10334151 and clave==1803:
        clavevalida=True
    else:
        print("clave invalida")
        intentos+=1
    if intentos==3:
        print("tarjeta bloqueada")
        tarjeta="bloqueada"
        break
    if tarjeta=="bloqueada":
        break
    if clavevalida==True:
        if monto>saldoinicialcajero:
            print("monto no permitido")
        if monto<=saldoinicialcajero:
            saldoinicialcajero=saldoinicialcajero-monto
            cuentausuario=cuentausuario-monto
            if cuentausuario<0:
                print("monto no permitido")
            else:
                billetes_de_20=monto//20000
                resto=monto%20000
                billetes_de_10=resto//10000
                resto=resto%10000
                billetes_de_5=resto//5000
                resto=resto%5000
                if (billetes_de_20<=carga_de_20 and billetes_de_10<=carga_de_10 and
                    billetes_de_5<=carga_de_5):
                    print("saldo cuenta="+str(cuentausuario))
                    print("saldo cajero="+str(saldoinicialcajero))
                    print("billetes 20000="+str(billetes_de_20))
                    print("billetes 10000="+str(billetes_de_10))
                    print("billetes 5000="+str(billetes_de_5))