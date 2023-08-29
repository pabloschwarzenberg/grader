n=int(input("Ingrese un mumero de hasta cuatro digitos:"))
a=int(n//10)
b=int(n%10)
c=int(n//100)
d=int((n%100)//10)
e=int(n//1000)
f=int((n%1000)//100)

if 0<=n<=9:
    print(n,"U")
elif 10<=n<=99:
    print(a,"D", "+", b,"U")
elif 100<=n<=999:
    print(c,"C", "+",d,"D","+",b,"U")
elif 1000<=n<=9999:
    print(e,"M","+",f,"C","+",d,"D","+",b,"U")