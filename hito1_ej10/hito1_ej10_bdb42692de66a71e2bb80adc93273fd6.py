#cajero automatico1
sui=100000
sci=1000000
opcion=0
while(opcion==0):
 u=print("usuario:10334151")
 c = int(input("ingrese la clave: "))
 contador = 0
 while (c != 1803 and contador < 3):
   print("clave invalida")
   c = int(input("ingrese la clave nuevamente: "))
   contador = contador + 1
   if (contador == 2):
    print("tarjeta bloqueada")
 if (c == 1803):
   mr = int(input("ingrese el monto que desea retirar: "))
   if (mr > 100000):
     print("monto no permitido")
   else:
    print("usted a retirado $", mr)
    print("saldo cuenta: ", sui - mr)
    print("saldo cajero: ", sci - mr)
sui = sui - mr
sci = sci - mr
o=input("desea continuar? N:si, S:no")
o=o.upper()
S=1
N=0
if(o==S):
 print("adiós")
else:
 opcion=0