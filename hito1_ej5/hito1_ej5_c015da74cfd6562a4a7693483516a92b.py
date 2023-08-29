#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese rut sin el digito verificador:"))
a=(rut%10)*2
b=((rut%10**2)//10)*3
c=((rut%10**3)//10**2)*4
d=((rut%10**4)//10**3)*5
e=((rut%10**5)//10**4)*6
f=((rut%10**6)//10**5)*7
g=((rut%10**7)//10**6)*2
h=((rut%10**8)//10**7)*3
total=a+b+c+d+e+f+g+h
x=total%11
z=11-x
if z==11:
    z=0

elif z==10:
    z="k"
    
    
print("dv=",z)      