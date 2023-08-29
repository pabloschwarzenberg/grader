# completa el código de la función
def amigos(a,b):
   suma_a=0
   suma_b=0
   for i in range(1,a):
       if a%i==0:
            suma_a+=i
 
   for x in range(1,b):
       if b%x==0:
            suma_b+=x
   return suma_a==b and suma_b==a