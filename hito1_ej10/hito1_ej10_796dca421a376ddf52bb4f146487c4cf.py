#Cajero Automático
sc=1000000
scu=100000
cuenta='10334151'
clave='1803'
cu_user=input(':')
c=0
while True:
   pw_user=input(':')
   if pw_user==clave:
       monto=int(input(':'))
       if monto<0 and monto>scu:
           print("monto no permitido")
       else:
           sc-=monto
           scu-=monto
           print('saldo cuenta=',scu)
           print('saldo cajero=',sc)
           break
   elif pw_user=='N':
       break
   else:
       c+=1
       print('error')
       if c==3:
           print('tarjeta bloqueada')
           break     