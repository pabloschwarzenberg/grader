#Cajero Automático
#U:10334151 clave:1803
SaldoCajero=1000000
#print("saldo total del cajero:",SaldoCajero)
usuario=int(input("ingrese su usuario: "))
while usuario!=10334151:
    usuario=int(input("error,Ingrese usuario: "))
claveU=0
i=0
#while not i==3 and claveU==1803:
while not claveU==1803:
    i=1+1
    claveU=int(input("ingrese la clave: "))
    #if clave==1803:
    if i ==3:
        print("Clave bloqueada")
        break
saldoU=100000
retiro=int(input("¿cuanto desea retirar?"))
SaldoCajero=SaldoCajero-retiro
saldoU=saldoU-retiro
print("saldo cuenta=",saldoU) 
print("saldo cajero=",SaldoCajero)