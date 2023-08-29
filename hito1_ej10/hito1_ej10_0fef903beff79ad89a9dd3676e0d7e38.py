usuario=int(input("Ingrese su usuario:"))
clave=(int(input("Ingrese su clave:")))
saldoi=1000000
saldo2=100000

while usuario!=10334151 :
    usuario=int(input("ERROR. Ingrese usuario:"))
    
intentos=0    
while clave !=1803:
    intentos=intentos+1
    if intentos==3:
        print("Suficientes intentos, tarjeta bloqueada.")
        break
    else:
        clave=int(input("Ingrese su clave nuevamente:"))
if intentos!=3:
    respuesta="s"
    while respuesta=="s":
        
        monto=int(input("Ingrese el monto a retirar:"))
        if monto>saldoi and monto>saldo2:
            print("monto no permitido")
        cal=saldo2-monto
        cal2=saldoi-monto
        print("saldo cuenta="+str(cal))
        print("saldo cajero="+str(cal2))
        respuesta=input("Quiere operar nuevamente?\n (s) Para volver a operar\n (n)Para salir.")