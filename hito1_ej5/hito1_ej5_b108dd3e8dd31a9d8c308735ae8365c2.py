#Cálculo del dígito verificador de un rut
a=int(input("ingrese rut sin el digito verificador:"))

x=(a//10000000)*3
y=((a//1000000)%10)*2
z=((a//100000)%10)*7
u=((a//10000)%10)*6
v=((a//1000)%10)*5
w=((a//100)%10)*4
r=((a//10)%10)*3
s=((a//1)%10)*2

b=(x+y+z+u+v+w+r+s)

RST1= b//11
RST2= b-(11*RST1)
dv=11-RST2

if dv==11:
    print("dv=0")
else:
    if dv==10:
        print("dv=k")
    else:
        print("dv=", dv)      