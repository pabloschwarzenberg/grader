#Cálculo del dígito verificador de un rut
r=int(input("Ingrese su rut:"))
x=((r//1)%10)*2
y=((r//10)%10)*3
z=((r//100)%10)*4
a=((r//1000)%10)*5
b=((r//10000)%10)*6
c=((r//100000)%10)*7
d=((r//1000000)%10)*2
e=((r//10000000)%10)*3
suma=(x+y+z+a+b+c+d+e)
resta1= suma//11
resta2=suma-(11*resta1)
resultado=11-resta2
if resultado==11:
    print("dv=0")
elif resultado==10:
    print("dv=K")
else:
    print("dv=",resultado)