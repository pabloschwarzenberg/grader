#Descomponer un número
x=int(input())
a=x//1000 
b=(x//100)-a*10
c=(x//10)- (a*100)- b*10
d=x-(a*1000)-(b*100)-c*10
print(a,"M","+",b,"C","+",c,"D","+",d,"U",)

