def es_primo (n):
 primo = True
 for i in range(2,n):
  if n%i ==0:
   primo = False
 if n == 1:
   primo = False
 
 
 return primo