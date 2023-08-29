#Cálculo del dígito verificador de un rut
n=str(input("Ingrese el RUT:"))
l=len(n)
r=l-1
m=9
b=0
c=0
for i in range(0,l+1):
    if m>=4:
        print("m",m)
        s=int(n[r-c])
        print("s",s)
        a=s*m
        b=a+b
        c+=1
        m-=1
        print("a",a,"b",b)
    else:
        m+=6
print(b)
resto=b%11
digito=11-resto
if resto==10:
    print("dv=k")
else:
    print("dv=",resto)

