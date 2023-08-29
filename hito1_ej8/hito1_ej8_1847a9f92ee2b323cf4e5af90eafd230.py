#Descomponer un número
n=int(input())
m=n//1000
z=n%1000
c=z//100
x=z%100
d=x//10
u=x%10
print(m,"M","+",c,"C","+",d,"D","+",u,"U")
