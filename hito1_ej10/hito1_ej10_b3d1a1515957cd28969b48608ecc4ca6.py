#Cajero Automático
intentos=3
saldocajero=1000000
saldocuenta=100000
while (intentos > 0):
   usuario=input("ingrese su usuario: ")
   contraseña=input("ingrese su contraseña: ")
   if (usuario=="10334151") and  (contraseña=="1803"):
        print("bienvenido")
        print("saldo actual 100000")
        montoaretirar=int(input("monto a retirar: "))
        if (montoaretirar > 0) and (montoaretirar<saldocuenta):
            saldocuenta=saldocuenta-montoaretirar
            saldocajero=saldocajero-montoaretirar
            print("tu nuevo saldo es",saldocuenta)
            break
        else:
            print("monto no permitido")
        
   
        
   else:
        print("clave invalida")
        intentos=int(intentos-1)
        if (intentos==0):
            print("tarjeta bloqueada")