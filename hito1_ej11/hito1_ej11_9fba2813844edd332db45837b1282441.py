c20 = 20 
c10 = 40 
c5 = 40
totalcajero = (c20*20000)+(c10*10000)+(c5*5000)
saldousuario = 100000
clave = 1803
intento = 3
acceso = 0
usuario = int(input("ingrese usuario: "))
while intento >0:
    intentclave = int(input("ingrese su clave")) 
    if intentclave != clave:
        intento -= 1 
    if intentclave ==clave:
        acceso = 1
        break
if acceso == 1:
    retirar = int(input("ingrese monto a retirar: "))
    constanteretirar = retirar
    cr20 = retirar//20000
    retirar -= cr20*20000
    cr10 = retirar//10000
    retirar -= cr10*10000
    cr5 = retirar//5000
    retirar -= cr5 * 5000
    totalcajero = totalcajero - constanteretirar
    saldousuario = saldousuario - constanteretirar
    print("saldo cuenta="+str(saldousuario))
    print("saldo cajero="+str(totalcajero))
    print("billetes 20000=",cr20)
    print("billetes 10000=",cr10)
    print("billetes 5000=",cr5)