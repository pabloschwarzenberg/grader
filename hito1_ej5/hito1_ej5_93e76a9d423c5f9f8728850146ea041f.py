#Cálculo del dígito verificador de un rut
n=int(input("Ingresar numero RUT:"))
a=(n//10**7)*3
b=((n//10**6)%10)*2
c=((n//10**5)%10)*7
d=((n//10**4)%10)*6
e=((n//10**3)%10)*5
f=((n//10**2)%10)*4
g=((n//10**1)%10)*3
h=(n%10)*2
x=(a+b+c+d+e+f+g+h)%11
dv=11-x
if dv==11:
    print("dv=0")
else:
    print("dv={}".format(dv))
if dv==10:
    print("dv=k")
else:
    print("dv={}".format(dv))
