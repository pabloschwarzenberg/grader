#Cálculo del dígito verificador de un rut
r=int(input("ingrese rut:"))
a=r//10000000
b=(r-10000000*a)//1000000
c=(r-10000000*a-1000000*b)//100000
d=(r-10000000*a-1000000*b-100000*c)//10000
e=(r-10000000*a-1000000*b-100000*c-10000*d)//1000
f=(r-10000000*a-1000000*b-100000*c-10000*d-1000*e)//100
g=(r-10000000*a-1000000*b-100000*c-10000*d-1000*e-100*f)//10
h=(r-10000000*a-1000000*b-100000*c-10000*d-1000*e-100*f-10*g)
i=3*a
j=2*b
k=7*c
l=6*d
m=5*e
n=4*f
o=3*g
p=2*h
s=i+j+k+l+m+n+o+p
t=s//11
u=t*11
v=s-u
w=11-v
if (w==10):
  print("dv="+str("k"))
if (w==11):
  print("dv="+str("0"))
else:
    print("dv="+str(w))
  
    
  