rut=int(input("dame tu rut "))
d1=rut//10000000
a1=d1*10000000
d2=((rut-a1)//1000000)
a2=d2*1000000
d3=((rut-a1-a2)//100000)
a3=d3*100000
d4=((rut-a1-a2-a3)//10000)
a4=d4*10000
d5=((rut-a1-a2-a3-a4)//1000)
a5=d5*1000
d6=((rut-a1-a2-a3-a4-a5)//100)
a6=d6*100
d7=((rut-a1-a2-a3-a4-a5-a6)//10)
a7=d7*10
d8=rut-a1-a2-a3-a4-a5-a6-a7

b8=2*d8
b7=3*d7
b6=4*d6
b5=5*d5
b4=6*d4
b3=7*d3
b2=2*d2
b1=3*d1

suma=b1+b2+b3+b4+b5+b6+b7+b8

c=(suma%11)
e=11-c

if e==11:
    print("dv="+"0")
elif e==10:
    print("dv="+"K")
else:
    print("dv=",e)
