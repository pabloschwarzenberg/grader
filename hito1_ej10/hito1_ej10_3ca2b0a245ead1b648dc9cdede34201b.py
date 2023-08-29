#Cajero Automatico
#Entrada
clave=int(input("Introdzca su clave: "))
saldoCajero=1000000
saldoCuenta=100000

i=1
while clave!= 1803 and i<3:
    clave=int(input("Clave incorrecta, intente nuevamente: "))
    i=i+1
    if clave != 1803 and i==3:
        print("Tarjeta Bloqueada")
i=3
retiro= int(input("Introduzca el monto que desea retirar: "))
if retiro <= saldoCuenta:
    saldoCuenta= saldoCuenta - retiro
    print("Saldo cuenta=", saldoCuenta)
    
    saldoCajero= saldoCajero - retiro
    print("Saldo cajero=", saldoCajero)
    
else:
    print("Monto no permitido")

