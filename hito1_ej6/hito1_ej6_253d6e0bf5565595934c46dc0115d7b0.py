n1 = int(input("Primer Numero:",))
n2 = int(input("Segundo Numero:",))
n3 = int(input("Tercer Numero:",))
if n1 <= n2 and n1 <= n3:
 if n2 <= n3:
   print (n1,",",n2,",",n3)
 if n3 <= n2:
   print (n1,",",n3,",",n2)
if n2 <= n1 and n2 <= n3:
 if n1 <= n3:
   print (n2,",",n1,",",n3)
 if n3 <= n1:
   print (n2,",",n3,",",n1)
if n3 <= n2 and n3 <= n1:
 if n2 <= n1:
   print (n3,",",n2,",",n1)
 if n1 <= n2:
   print (n3,",",n1,",",n2)