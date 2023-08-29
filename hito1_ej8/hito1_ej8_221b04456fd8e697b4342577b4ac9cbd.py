#Descomponer un número
a=int(input("numero"))
u=a%10
d=(a%100)//10
c=(a%1000)//100
m=(a%10000)//1000
print(m,"M + ",c,"C + ",d,"D + ",u,"U")