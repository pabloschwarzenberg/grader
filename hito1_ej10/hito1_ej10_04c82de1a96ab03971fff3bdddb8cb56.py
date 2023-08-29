#Cajero Automático
import sys
usuario=int(input("Ingrese usuario: "))
saldo_caj=1000000
saldo_per=100000
clave=int(input("Ingrese clave: "))
cont=1
if usuario==10334151:
     while clave!=1803:
         if cont==1:
               print("Le quedan 2 intentos")
         if cont==2:
               print("Le queda un intento")
         cont=cont+1
         clave=int(input("Ingrese clave nuevamente: "))
         if cont>3:
               print("Su tarjeta ha sido bloqueada")
               sys.exit(1)
monto=int(input("Ingrese monto a sacar: "))
while monto>100000:
 print("Monto invalido")
 monto=int(input("Ingrese monto a sacar: "))
if monto<=saldo_per:
    perso=saldo_per-monto
    caje=saldo_caj-monto
    print("Transacción exitosa")
    print("saldo cuenta=",perso)
    print("saldo cajero=",caje)
 
          