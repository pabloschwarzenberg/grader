n1=int(input("ingrese numero de hasta 4 digitos: "))
n=str(n1)
if (n1<10000 and n1>=1000):
    a=int((n[0:1]))
    c=str(n[1:2])
    d=str(n[2:3])
    e=str(n[3:4])  
    print(a,"M+",c,"C +",d,"D +",e,"U")
if n1<1000 and n1>=100:
    a=str((n[0:1]))
    c=str(n[1:2])
    d=str(n[2:3])
    print(a,"C +",c,"D +",d,"U")
if n1<100 and n1>=10:
    a=str((n[0:1]))
    c=str(n[1:2])
    print(a,"D +",c,"U")
if n1<10:
     a=str((n[0:1]))
     print(a,"U")