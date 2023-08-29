#Ordenar tres números
A = int(input("Ingrese 1er numero: "))
B = int(input("Ingrese 2do numero: "))
C = int(input("Ingrese 3er numero: "))

if A > B:
   if B > C:
      print (C,",",B,",",A)
   else:
      if A > C: 
         print (B,",",C,",",A)
      else:
         print (B,",",A,",",C)
else:
   if A > C:
      print (C,",",A,",",B)
   else:
      if B > C:
         print (A,",",C,",",B)
      else:
         print (A,",",B,",",C)
       