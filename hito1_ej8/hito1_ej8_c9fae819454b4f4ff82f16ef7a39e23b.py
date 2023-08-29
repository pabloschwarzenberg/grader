#Descomponer un número
n=int(input("ingrese un numero para desconponer"))
m=n//1000
c=(n//100)%10
d=(n//10)%10
u=n%10
if(m>0) and (c>=0) and (d>=0) and (u>=0):
    print(m,"M +",c,"C +",d,"D +",u,"U")
elif(c>0) and (d>=0) and (u>=0):
    print(c,"C +",d,"D +",u,"U")
elif(d>0) and (u>=0):
    print(d,"D +",u,"U")
elif(u>0):
    print(u,"U")    