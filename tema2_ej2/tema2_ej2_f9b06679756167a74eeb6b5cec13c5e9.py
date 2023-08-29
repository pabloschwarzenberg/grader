# completa el código de la función
def suma(N,S):
       for i in range(1,N):
             print("i",i,"rango", range(1,N))
             if(N % i==0):
                    print("valor n: ",N)
                    S=S+i
                    print("valor S: ",S)
       return S
sum1,sum2=0,0
n1=3
n2=2
sum1 = suma(n1, sum1)
sum2 = suma(n2, sum2)
if((sum1==n2)and (sum2==n1)):
return True
else:
return False
           