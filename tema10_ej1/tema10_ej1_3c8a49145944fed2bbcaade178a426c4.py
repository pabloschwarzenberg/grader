def mcm(a, b, ab):
   """Esta función recibe dos enteros y devuelve el multiplo comum"""

   # cogemos el mayor de los dos
   if a > b:
       mayor = a
   else:
       mayor = b

   while(True):
       if((mayor % a == 0) and (mayor % b == 0)):
           mcm = mayor
           break
       mayor += 1

   return mcm

if __name__=="__main__":
    print(mcm(88,44,88*44))
           