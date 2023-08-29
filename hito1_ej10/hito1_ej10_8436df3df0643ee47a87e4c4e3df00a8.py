saldoI=1000000
saldoW=100000
retiro=0

usuario = int(input("Ingrese su usuario: "))
clave = int(input("Ingrese su clave: "))

saldoW = saldoW - retiro
saldoI = saldoI - retiro

print("Saldo disponible del cajero:",saldoI)
if usuario == 10334151 and clave == 1803:
    print("Saldo disponible cuenta corriente:",saldoW)
    retiro = int(input("Ingrese la cantidad para retirar: "))
    if retiro > saldoW:
        print("No tienes suficiente saldo")
    elif retiro > saldoI:
            print("No puede retirar esa cantidad")
    else: 
        saldoW = saldoW - retiro
        saldoI = saldoI - retiro
        print("Saldo cuenta={}, Saldo cajero={}".format(saldoW, saldoI))
else:
    print("Clave invalida")
