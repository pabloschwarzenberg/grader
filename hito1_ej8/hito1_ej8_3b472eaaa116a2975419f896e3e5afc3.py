#Descomponer un número
n=input()
u=((eval(n)%10)//1)
d=((eval(n)%100)//10)
c=((eval(n)%1000)//100)
m=((eval(n)%10000)//1000)
if len(n)==1:
    print(u,"U")
elif len(n)==2:
    print(d,"D","+",u,"U")
elif len(n)==3:
    print(c,"C","+",d,"D","+",u,"U")
else:
    print(m,"M","+",c,"C","+",d,"D","+",u,"U")     