#Cajero Automático
SC=1000000
SCU=100000
cuenta='10334151'
clave='1803'
cu_user=input(':')
c=0
while True:
   pw_user=input(':')
   if pw_user==clave:
      monto=int(input(':'))
      if monto<0 and monto>SCU:
         print("monto no permitido")
      else:
         SC-=monto
         SCU-=monto
         print("saldo cuenta=",SCU)
         print("saldo cajero=",SC)
         break
   elif pw_user=='N':
        break
   else:
        c+=1
        print('error')
        if c==3:
           print('targeta bloqueada')
           break
