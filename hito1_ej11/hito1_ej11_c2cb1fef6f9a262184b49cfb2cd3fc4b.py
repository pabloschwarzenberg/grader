c20 = 20
c10 = 40
c5 = 40
totalCajero = (c20*20000)+(c10*10000)+(c5*5000)
saldo_usuario= 100000 # Cien mil
clave = 1803
intento = 3
acceso = 0
usuario = int(input("Ingrese usuario"))
while intento > 0:
    intentclave = int(input("Ingrese su clave: "))
    if intentclave != clave:
        intento = intento-1
    if intentclave == clave:
        acceso = 1
        break
if acceso == 1:
    retirar = int(input("Ingrese monto a retirar"))
    constateRetirar = retirar
    cr20 = retirar//20000
    retirar -= cr20*20000
    cr10 = retirar//10000
    retirar -= cr10*10000
    cr5 = retirar//5000
    retirar -= cr5*5000
    print("Billetes 20000="+str(cr20))
    print("Billetes 10000="+str(cr10))
    print("Billetes 5000="+str(cr5))
    totalCajero = totalCajero - constateRetirar
    saldo_usuario = saldo_usuario - constateRetirar
    print("saldo cuenta="+str(saldo_usuario))
    print("saldo cajero="+str(totalCajero))