def amigos(a,b):
  divisoresa=[]
  divisoresb=[]
  for i in range(1,a+1):
   if a%i==0 and a/i!=1:
    divisoresa.append(i)    
  for n in range(1,b+1):
   if b%n==0 and b/n!=1:
    divisoresb.append(n)
  numero_a=0
  numero_b=0
  for x in divisoresa:
   numero_a=numero_a + x
  for z in divisoresb:
   numero_b=numero_b + z
  if numero_a==b and numero_b==a:
   return True
  else:
   return False