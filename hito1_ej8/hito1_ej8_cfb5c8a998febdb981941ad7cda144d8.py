#Descomponer un número
n=int(input())
m=n//1000
c=(n-m*1000)//100
d=(n-m*1000-c*100)//10
u=n%10
print(m,"M+",c,"C+",d,"D+",u,"U")