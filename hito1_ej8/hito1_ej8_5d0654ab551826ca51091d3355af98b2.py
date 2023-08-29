#Descomponer un número
num1=int(input())

m1=(num1//1000)
c1=((num1%1000)//100)
d1=((num1%100)//10)
u1=(num1%100)%10

if num1>=1000:
    print(m1,"M +",c1,"C +",d1,"D +",u1,"U")
elif 100<=num1<1000:
    print(c1,"C +",d1,"D +",u1,"U")
elif 10<=num1<100:
    print(d1,"D +",u1,"U")
elif num1<10:
    print(u1,"U")



