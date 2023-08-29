#Cajero Automático
#salidas
#  -mensaje clave invalida 
#  -saldo con el que queda la cuentadel usuario y en el cajero
#  -Tarjeta bloqueada
#  -monto no permitido


saldocajero=1000000
saldoinicial=100000
usuario=int(input("ingrese su usuario:"))
while usuario !=10334151: #validar usuario
      usuario = int(input("error, ingrese usuario:"))
                    
claveusuario=int(input("ingrese su clave:"))
contador=0
while not(claveusuario==1803):#clave!1803
      contador= contador+1
      if contador==3:
       print("tarjeta bloqueada")
       break
      else:
        claveusuario=int(input("ingrese su clave:"))
if contador !=3:#(esta se ejecuta cuando la clave es correcta y intentos <=3) o cuando los intentos =3
 

  montoaretirar=int(input("ingrese su monto:"))
  if montoaretirar<=saldocajero:
      if montoaretirar<=saldoinicial:
         saldocajero=saldocajero-montoaretirar
         saldoinicial=saldoinicial-montoaretirar
         print("saldo cuenta=",saldoinicial)
         print("saldo cajero=",saldocajero)
      else:
          print("monto invalido")
else:
      print("monto invalido")     