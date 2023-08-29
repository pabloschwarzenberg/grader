#Descomponer un número
a=int(input("Ingrese número:"))
if a>=1000 and a<10000:
    b=str(a)
    c=b[3]
    d=b[2]
    e=b[1]
    f=b[0]
    print(f,"M","+",e,"C","+",d,"D","+",c,"U")
elif a>=100 and a<1000:
    b=str(a)
    c=b[2]
    d=b[1]
    e=b[0]
    print(e,"C","+",d,"D","+",c,"U")
elif a>=10 and a<100:
    b=str(a)
    c=b[1]
    d=b[0]
    print(d,"D","+",c,"U")
elif a>=1 and a<10:
    b=str(a)
    c=b[0]
    print(c,"U")