#Factores Primos
def factores_primos(numero):
     divisor=2
     while divisor<=numero:
         if numero%divisor==0:
             i=0
             while i<=divisor:
                 if divisor%i==0:
                     i=i+1
                     if i==2:
                        return divisor
                     else:
                        return False
         divisor=divisor+1
int(input())=factores_primos
print(divisor)