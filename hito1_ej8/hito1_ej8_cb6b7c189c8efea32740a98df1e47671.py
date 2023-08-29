#Descomponer un número
x=int(input())

m1=x//1000
c1=(x%1000)//100
d1=(x%100)//10
u1=(x%10)

print(m1,"M +",c1,"C +",d1,"D +",u1,"U")