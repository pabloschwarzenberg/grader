#Descomponer un número
numero1=int(input())
a=numero1/1000
a1=numero1%1000
a11=a1/100
a2=a1%100
a22=a2/10
b=numero1/100
b1=numero1%100
b11=b1/10
c=numero1/10
d=numero1/1

if a>=1 and a<10:
    print(int(a),"M","+",int(a11),"C","+",int(a22),"D","+",a2%10,"U")
elif b>=1 and a<10:
    print(int(b),"C","+",int(b11),"D","+",b1%10,"U")
elif c>=1 and a<10:
    print(int(c),"D","+",c%10,"U")
elif d>=1 and a<10:
    print(int(d),"U")

      