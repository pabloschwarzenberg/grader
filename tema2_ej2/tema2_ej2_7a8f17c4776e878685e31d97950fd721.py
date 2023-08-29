# completa el código de la función
def suma(a,b):
       for i in range(2,a):
             if(a % i==0):
                    b=b+i
       return b
sum1,sum2=1,1
sum1 = suma(n1, sum1)
sum2 = suma(n2, sum2)
if((sum1==n2)and (sum2==n1)):
       print(True)
else:
       print(False)