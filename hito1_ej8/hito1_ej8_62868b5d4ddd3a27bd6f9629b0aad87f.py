#Descomponer un número
n=int(input("ingrese numero:"))

if (n//1000)>=1:
    m=n//1000
    c=n//100-m*10
    d=n//10-m*100-c*10
    u=n-m*1000-c*100-d*10
    print(m,"M","+",c,"C","+",d,"D","+",u,"U")

if 10>(n//100)>=1:
    c=n//100
    d=n//10-c*10
    u=n-c*100-d*10
    print(c,"C","+",d,"D","+",u,"U")
    

if 10>(n//10)>=1:
   
    d=n//10
    u=n-d*10
    print(d,"D","+",u,"U")

else:
    print(n,"U")
          