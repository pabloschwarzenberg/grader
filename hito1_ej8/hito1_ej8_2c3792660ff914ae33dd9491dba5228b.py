#Descomponer un número
n=int(input())

m=n//1000
c=(n//100)%10

d=n%100
d=d//10


u=n%10

print(m,"M +",c,"C +",d,"D +",u,"U") 