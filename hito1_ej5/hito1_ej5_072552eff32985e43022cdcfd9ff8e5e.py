#Cálculo del dígito verificador de un rut
rut=int(input("Rut: "))
a=rut//10000000
aa=a%10
b=rut//1000000
bb=b%10
c=rut//100000
cc=c%10
d=rut//10000
dd=d%10
e=rut//1000
ee=e%10
f=rut//100
ff=f%10
g=rut//10
gg=g%10
h=rut//1
hh=h%10
i=aa*3+bb*2+cc*7+dd*6+ee*5+ff*4+gg*3+hh*2
j=i%11
m=11-j
if m==10:
    print("dv=k")
elif m==11:
    print("dv=0")
else:
    print("dv="+str(m))

