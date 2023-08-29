#Factores Primos
def descomponer(p):
   primos=[]
   for i in range(2, p+1):
       while p % i == 0:
           primos.append(i)
           p = p / i
   return primos
 