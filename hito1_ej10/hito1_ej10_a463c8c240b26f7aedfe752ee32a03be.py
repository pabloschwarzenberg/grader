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