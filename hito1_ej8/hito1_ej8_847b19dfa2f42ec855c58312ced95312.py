#Descomponer un número
n=int(input())
u=(n%10)
d=((n%100)-(n%10))//10
c=((n%1000)-(n%100))//100
m=((n%10000)-(n%1000))//1000
if (m==0):
    print(c,"C","+",d,"D","+",u,"U")
elif (m==0) and (c==0):
    print(d,"D","+",u,"U")
elif (m==0) and (c==0) and (d==0): 
    print(u,"U")
else:    
    print(m,"M","+",c,"C","+",d,"D","+",u,"U")
