#Descomponer un número
a1=int(input())
a=a1//1000
b=(a1//100)-(a*10)
c=(a1//10)-(a*100)-(b*10)
d=a1-(a*1000)-(b*100)-(c*10)
print(a,"M+",b,"C+",c,"D+",d,"U")      