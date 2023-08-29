#Cálculo del dígito verificador de un rut
rut=int(input())

h=(rut-(rut//10)*10)*2
g=(rut//10-(rut//100)*10)*3
f=(rut//100-(rut//1000)*10)*4
e=(rut//1000-(rut//10000)*10)*5
d=(rut//10000-(rut//100000)*10)*6
c=(rut//100000-(rut//1000000)*10)*7
b=(rut//1000000-(rut//10000000)*10)*2
a=(rut//10000000)*3

d=11-((a+b+c+d+e+f+g+h)%11)

if d==11:
    d=0

if d==10:
    d="k"


print("dv=",d)
