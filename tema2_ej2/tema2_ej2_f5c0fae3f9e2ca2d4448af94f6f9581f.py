#DEFINICÓN DE FUNCIÓN

def amigos(a,b):
   DivNum1 =[]

   for i in range (1,a + 1):
      if a % i == 0:
         DivNum1.append(i)

   Total1 = 0

   for i in DivNum1:
      Total1 = Total1 + i


   DivNum2 =[]

   for i in range (1,b + 1):
      if b % i == 0:
         DivNum2.append(i)

   Total2 = 0

   for i in DivNum2:
      Total2 = Total2 + i
                
   if a == b:
      return False

   elif Total1 == Total2:
      return True
 
   else:
      return False


