#Descomponer un número
n=int(input())
m=int(n/1000)
c=int((n-m*1000)/100)
d=int((n-m*1000-c*100)/10)
u=int(n-m*1000-c*100-d*10)
print(m,"M +",c,"C +",d,"D +",u,"U")