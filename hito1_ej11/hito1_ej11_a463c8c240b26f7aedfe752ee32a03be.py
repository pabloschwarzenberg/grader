#Cajero Automático
usuario=int(input("ingrese su numero de usuario "))
clave=int(input("ingrese su clave "))    
while usuario!=10334151:
    usuario=int(input("ingrese nuevamente su numero de usuario "))
while clave!=1803:
    clave=int(input("ingrese nuevamente su clave "))
retirar=int(input("cuanto desea retirar "))
scinicial=1000000
saldousuario=100000
resta=saldousuario-retirar
restacajero=scinicial-retirar
while clave!=1803:
    clave=int(input("confirme su clave "))
while retirar<0:
    retirar=int(input("monto no permitido"))
if retirar>0 and retirar<100000: 
    print("saldo cuenta=", resta)
    print("saldo cajero=", restacajero)
if retirar >=20000:
    queda=retirar//20000
    print("billetes 20000="+str(queda))
    retirar=retirar%20000
if retirar >=10000:
    queda=retirar//10000
    print("billetes 10000="+str(queda))
    retirar=retirar%10000
if retirar >=5000:
    queda=retirar//5000
    print("billetes 5000="+str(queda))
    retirar=retirar%5000