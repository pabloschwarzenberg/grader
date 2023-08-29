#Descomponer un número
n=int(input("Ingrese número: "))

if n/1000>=1:
    a=n//1000
    b=(n-a*1000)//100
    c=(n-a*1000-b*100)//10
    d=(n-a*1000-b*100-c*10)//1
    print(a,"M+",b,"C+",c,"D+",d,"U")
elif n/100>=1:
    b=n//100
    c=(n-b*100)//10
    d=(n-b*100-c*10)//1
    print(b,"C+",c,"D+",d,"U")
elif n/10>=1:
    c=n//10
    d=(n-c*10)//1
    print(c,"D+",d,"U")
else:
    d=d
    print(d,"U")      