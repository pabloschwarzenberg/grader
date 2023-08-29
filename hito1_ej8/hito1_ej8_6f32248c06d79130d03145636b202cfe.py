#Descomponer un número
a = int(input("Ingrese un numero hasta 4 digitos: "))
if a < 100:
    b = a//10**1
    c = (a%10**1)%10**1
    print(b,"D","+",c,"U")
elif a >= 100 and a < 1000:
    d = a//10**2
    e = ((a%10**2)%10**2)//10**1
    f = ((a%10**3)%10**2)%10**1
    print(d,"C","+",e,"D","+",f,"U")
else:
    if a >= 1000:
        g = a//10**3
        h = ((a%10**3)%10**3)//10**2
        i = ((a%10**3)%10**2)//10**1
        j = ((a%10**3)%10**2)%10**1
        print(g,"M","+",h,"C","+",i,"D","+",j,"u")