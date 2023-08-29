#Cajero Automático
saldoinicialcajero=1000000
cuentausuario=100000
intentos=0
salir=False
clavevalida=False
tarjeta=""

while clavevalida==False:
    usuario=int(input("ingrese nombre de usuario: "))
    clave=int(input("ingrese clave: "))
    monto=int(input("monto a retirar: "))
    terminar=input("terminar:")
    if terminar=="n" or terminar=="N":
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
                print("saldo cuenta="+str(cuentausuario))
                print("saldo cajero="+str(saldoinicialcajero))