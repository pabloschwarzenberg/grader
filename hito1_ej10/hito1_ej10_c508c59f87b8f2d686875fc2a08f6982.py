#Cajero Automático
usuario=int(input())
us=10334151
cajero=1000000
cuenta=100000
creal=1803
i=3
while usuario==us and i>0:
      clave=input()
      if clave==creal:
         monto=int(input())
         cuenta=int(cuenta)-int(monto)
         cajero=int(cajero)-int(monto)
         print("saldo cuenta=",cuenta)
         print("saldo cajero=",cajero)
      else:
         print ("clave invalida")
         if i==1:
            print ("tarjeta bloqueada")
         i=i-1

       