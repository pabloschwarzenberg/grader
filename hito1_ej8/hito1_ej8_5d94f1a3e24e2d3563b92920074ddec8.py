#Descomponer un número
n=int(input("ingrese numero:"))
x=n//1000
y=(n-(x*1000))//100
z=(n-(x*1000)-(y*100))//10
d=n-(x*1000)-(y*100)-(z*10)
if x==0 and y==0 and z==0 and d==0:
    print("0")
if x==0 and y==0 and z==0:
    print(d,"U")
if x==0 and y==0 and d==0:
    print(z,"D")
if x==0 and z==0 and d==0:
    print(y,"C")
if x==0:
   print(y,"C","+",z,"D","+",d,"U")
if y==0 and z==0 and d==0:
    print(x,"M")    
if x==0 and y==0:
    print(z,"D","+",d,"U")
    
if z==0 and d==0:
    print(x,"M","+", y,"C")

if x!=0 and y!=0 and z!=0 and d!=0:
    print(x,"M","+", y,"C","+",z,"D","+",d,"U")