#Descomponer un número
numero=int(input())
m=(numero//1000)
c=((numero//100)%10)
d=((numero//10)%10)
u=(numero%10)
if m==0:
   print(c,"C","+",d,"D","+",u,"U")
elif m==0 and c==0:
   print(d,"D","+",u,"U")
elif m==0 and c==0 and d==0:
   print(u,"U")
else:
   print(m,"M","+",c,"C","+",d,"D","+",u,"U")