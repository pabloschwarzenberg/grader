def numero_perfecto(n):
   divisor=1
   b=0
   while divisor<n:
      if n%divisor==0:
         b=b+divisor
      divisor=divisor+1
   if b==n:
      return True
   else:
       return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(n))
           