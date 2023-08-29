def amigos(a,b):
   diva=1
   divb=1
   sumaa=0
   sumab=0
   while diva<a:
      if a%diva==0:
         sumaa = sumaa+diva
      diva= diva+1
   print(sumaa)
   while divb<b:
      if b%divb==0:
         sumab = sumab+divb
      divb = divb+1
   print(sumab)
   if sumaa==b and sumab==a:
      return True
   else:
      return False