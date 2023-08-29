# completa el código de la función
def suma(N,S):
       for i in range(2,N):
             if(N % i==0):
                    S=S+i
       return S

a=int(input("ingrese primer numero"))
b=int(input("ingrese segundo numero"))

sum1,sum2=1,1
sum1 = suma(a, sum1)
sum2 = suma(b, sum2)
if((sum1==b) and (sum2==a)):
  return True
else:
  return False