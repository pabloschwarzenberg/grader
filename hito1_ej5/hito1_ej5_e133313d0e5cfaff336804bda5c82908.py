#Cálculo del dígito verificador de un rut
rut=int(input("ingrese su rut: "))
a=rut%10
b=(rut%100-a)//10
c=(rut%1000-rut%100)//100
d=(rut%10000-rut%1000)//1000
e=(rut%100000-rut%10000)//10000
f=(rut%1000000-rut%100000)//100000
h=(rut%10000000-rut%1000000)//1000000
i=(rut%100000000-rut%10000000)//10000000

a1=(a*2)
a2=(b*3)
a3=(c*4)
a4=(d*5)
a5=(e*6)
a6=(f*7)
a7=(h*2)
a8=(i*3)

z=a1+a2+a3+a4+a5+a6+a7+a8
x=(z//11)
r=z-(11*x)
dv=11-r

m="0"
n="K"

if dv==11:
    print("dv=0")
elif dv==10:
    print("dv=k")
else:
    print("dv= ",dv)
    

