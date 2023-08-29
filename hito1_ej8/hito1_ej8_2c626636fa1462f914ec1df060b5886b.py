x = int(input("Ingrese un número de hasta 4 dígitos:"))

a = ((x//1000)%10)
b = ((x//100)%10)
c = ((x//10)%10)
d = ((x//1)%10)

if x>=0 and x<=9:
    print(d,"U")
elif x>=10 and x<=99:
    print(c,"D+",d,"U")
elif x>=100 and x<=999:
    print(b,"C+",c,"D+",d,"U")
elif x>=1000 and x<=9999:
    print(a,"M+",b,"C+",c,"D+",d,"U")