#Cálculo del dígito verificador de un rut
rut=int(input("Rut: "))
b=rut//(10**6)
c=rut//(10**5)-10*b
d=rut//(10**4)-100*b-10*c
e=rut//(10**3)-1000*b-100*c-10*d
f=rut//(10**2)-10000*b-1000*c-100*d-10*e
g=rut//(10**1)-100000*b-10000*c-1000*d-100*e-10*f
h=rut-1000000*b-100000*c-10000*d-1000*e-100*f-10*g
dv=11-(11%(2*h+3*g+4*f+5*e+6*d+7*c+8*b))
if dv==10:
  print("dv=k")
else:
  print(dv)