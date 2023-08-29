#Cajero Automático
q=1000000
w=100000
cuenta='10334151'
clave='1803'
cu_user=input(':')
a=0
while True:
   pw_user=input(':')
   if pw_user==clave:
       monto=int(input(':'))
       if monto<0 and monto>w:
           print("monto no permitido")
       else:
           q-=monto
           w-=monto
           print('saldo cuenta=',w)
           print('saldo cajero=',q)
           break
   elif pw_user=='N':
       break
   else:
       a+=1
       print('error')
       if a==3:
           print('tarjeta bloqueada')
           break