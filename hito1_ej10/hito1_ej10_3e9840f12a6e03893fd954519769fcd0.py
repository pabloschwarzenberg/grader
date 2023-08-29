#Cajero Automático
saldo=1000000
cuenta=100000

inicio=0


while inicio<3:
    usuario=int(input("Ingrese su usuario:"))
    clave=int(input("Ingrese su clave:"))
    if usuario==10334151 and clave==1803:   
        print("Bienvenido!")
        inicio=3
    else:
        print("clave invalida")
        inicio=inicio+1
    if usuario!=10334151 and clave!=1803:  
        print("tarjeta bloqueada")

if usuario==10334151 and clave==1803:
    monto=int(input("Que monto desea retirar?:"))

if usuario==10334151 and clave==1803:
    if saldo>monto and cuenta>monto:
        saldo=saldo-monto
        cuenta=cuenta-monto
        print("saldo cuenta=",cuenta,"saldo cajero=",saldo)
    else:
        print("monto no permitido")