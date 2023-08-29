#Descomponer un número
r = str(input("ingrese un numero "))
c = int(r)
if len(r)==1:
    print(c,"U")
elif len(r)==2:
    d=c//10
    u=c%10
    print(d,"D+",u,"U")
elif len(r)==3:
    s=r[0]
    d=r[1]
    u=r[2]
    print(s,"C+",d,"D+",u,"U")
elif len(r)==4:
    m=r[0]
    s=r[1]
    d=r[2]
    u=r[3]
    print(m,"M+",s,"C+",d,"D+",u,"U")   