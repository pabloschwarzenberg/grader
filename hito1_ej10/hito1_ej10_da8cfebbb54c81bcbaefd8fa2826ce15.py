#U: 10334151 clave:1803
SaldoCajero=1000000
#print("Saldo total del cajero:", SaldoCajero)
usuario= int(input("Ingrese su usuario: "))
while usuario != 10334151:
    usuario = int(input("Error, Ingrese Usuario: "))
claveU=0
i=0
#while not i==3 and claveU==1803:
while not claveU == 1803:
    i=1+1
    claveU=int(input("ingrese la clave: "))
    #if clave==1803:
    if i == 3:
        print("Clave Bloqueada")
        break
SaldoU = 100000
retiro = int(input("¿Cúanto dinero desea retirar?: "))
SaldoCajero = SaldoCajero - retiro
SaldoU = SaldoU - retiro
print("Saldo Cuenta=", SaldoU)
print("Saldo Cajero=", SaldoCajero)