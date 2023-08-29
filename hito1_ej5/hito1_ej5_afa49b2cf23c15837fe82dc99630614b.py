rut=int(input("ingrese rut : "))
d1=rut%10
rut=rut//10

d2=rut%10
rut=rut//10

d3=rut%10
rut=rut//10

d4=rut%10
rut=rut//10

d5=rut%10
rut=rut//10

d6=rut%10
rut=rut//10

d7=rut%10
rut=rut//10

d8=rut%10


d1=d1*2
d2=d2*3
d3=d3*4
d4=d4*5
d5=d5*6
d6=d6*7
d7=d7*2
d8=d8*3

x=d1+d2+d3+d4+d5+d6+d7+d8

x=x%11

a=11-x

if a==11:
    a=0
    print("dv=",a)
elif a == 10:
    a="k"
    print("dv=",a)
else:
    print("dv=",a)