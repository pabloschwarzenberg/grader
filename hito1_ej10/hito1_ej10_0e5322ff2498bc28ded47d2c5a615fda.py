#Cajero Automático

intentos=0

usuario=10334151
clave=1803

monto_cajero=1000000
monto_cuenta=100000

print("Usuario 10334151")
      
while intentos < 3:
    y=int(input("Ingrese clave:"))

    intentos=intentos + 1

    if (y>clave) or (y<clave):
        print("clave invalidad")
    if(y==clave):
        break
    
retiro=0
resta=(monto_cuenta - retiro)
resta2=(monto_cajero - retiro)    

if (y==clave):
    retiro=int(input("Ingrese su monto:"))

else:
    if (retiro > 100000):
        print("monto no permitido")
    else:
        if (retiro < 100000):
            resta=str(resta)
            resta2=str(resta)
            print("Saldo cuenta="+resta)
            print("saldo cajero="+resta2)
        else:
            print("monto no valido")
      