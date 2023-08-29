#Descomponer un número
a=input()
x=int(a)
b=int((x/10))
d=int((x/100))
e=int((x/1000))
c=(a[::-1])
if(x<10):
 print(a,"U")
elif(100>x>=10):
 print(b,"D +",(c[0]),"U")
elif(1000>x>=100):
 print(d,"C +",(c[1]),"D +",(c[0]),"U")
elif(10000>x>=1000):
 print(e,"M +",(c[2]),"C +",(c[1]),"D +",(c[0]),"U")

 