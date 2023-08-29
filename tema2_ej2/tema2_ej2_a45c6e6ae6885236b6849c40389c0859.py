np = int(input("ingrese primer numero"))
nz = int(input("ingrese segundo numero"))
def suma(N,S):
       for i in range(2,N):
             if(N % i==0):
                    S=S+i
       return S
sum1,sum2=1,1
sum1 = suma(np, sum1)
sum2 = suma(nz, sum2)
       if((sum1==nz)and (sum2==np)): 
       return True
       else: 
       return False