#Cálculo del dígito verificador de un rut
rut=float(input("ingrese su rut: "))
d1=rut//10000000
a2=rut//1000000
d2=a2%10
a3=rut//100000
d3=a3%10
a4=rut//10000
d4=a4%10
a5=rut//1000
d5=a5%10
a6=rut//100
d6=a6%10
a7=rut//10
d7=a7%10
d8=rut%10
m1=d8*2
m2=d7*3
m3=d6*4
m4=d5*5
m5=d4*6
m6=d3*7
m7=d2*2
m8=d1*3
x=m1+m2+m3+m4+m5+m6+m7+m8
y=int(x/11)
l=y*11
z=x-l
q=11-z
if(q==11):
 print("dv=0")
if(q==10):
 print("dv=K")
else:
 print("dv=",q)
     