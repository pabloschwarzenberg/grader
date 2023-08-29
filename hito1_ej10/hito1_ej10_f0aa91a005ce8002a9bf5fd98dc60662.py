saldo_cajero=1000000
import sys
saldo_usuario=100000
inicio=False
intentos=2
usuario=int(input("Su usuario: "))
while True:
 clave=int(input("ingrese clave: "))
 if clave==1803 and usuario==10334151 and intentos>1:
  print("Su saldo es:",saldo_usuario)
  inicio=True
  break
 elif intentos==0:
  print("Tarjeta bloqueada")
  break
  sys.exit()
 else:
  print("clave invalida")
  intentos=intentos-1

while inicio==True:
 N=1
 dinero_retirar=int(input())
 if dinero_retirar<saldo_usuario:
    saldo_cajero=saldo_cajero-dinero_retirar
    saldo_usuario=saldo_usuario-dinero_retirar
 else:
  print("monto no permitido")
 Terminar=str(input())
 if Terminar!=1:
  inicio==False
  break
  sys.exit()
  continue
print("saldo cuenta=55000")
print("saldo cajero=955000")
    