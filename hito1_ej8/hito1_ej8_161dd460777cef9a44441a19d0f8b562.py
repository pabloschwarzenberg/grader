#Descomponer un número
n = int(input())
a = n 
u = 1%10
a = a//10
d = a%10
a = a//10
c = a%10
a = a//10
m = a
if (m == 0):
    print(c,"C +",d,"D +",u,"U")
elif (m == 0) and (c == 0):
    print(d,"D +",u,"U")
else:
    print(m,"M +",c,"C +",d,"D +",u,"U")