#Conversión de Decimal a Binario
N=input("   ddw")
n=0
a=0
r=0
while(a!=int(N)):
   a=a+1
   r=(9*r+1)/9
   if(int(r)!=r):
        j=int(r)
        j=j/10
        if(int(r)!=r):
         while(int(j)!=j):
            j=int(j)/10
            n=n+1   
   r=((j*10)+1)*(10**n)
   n=0       
print("resultado=",r)      