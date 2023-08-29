#Cajero Automático
saldo=1000000
saldoC=100000
billetes=[20000,10000,5000,1000]
user="10334151"
pw="1803"
cuenta=input("cuenta:")
c=0
while True:
   pwl=input("contraseña:")
   if pwl==pw:
      monto=int(input("monto a retirar:"))
      if monto>saldoC or monto<0:
         print("monto no permitido")
      else:
         saldoC-=monto
         saldo-=monto
         print("saldo cuenta={0}\nsaldo cajero={1}".format(saldoC,saldo))
         for x in billetes:
            c=0
            pasar=monto//x
            if pasar>0:
               for a in range(pasar):
                  monto-=x
                  c+=1
            else:
               continue
            print("billetes",x,"=",c)
            if monto==0:
               break
         print("faltan:",monto)
         break
      if pwl=="N":
          break
      else:
          c+=1
          print("error")
          if c==3:
             print("targeta bloqueada")
             break