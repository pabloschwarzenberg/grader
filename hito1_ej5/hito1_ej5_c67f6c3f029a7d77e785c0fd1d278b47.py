rut=str(input())

if len(rut)==7:
    rut=str(0) + rut
else:
    rut=rut

p1=rut[-1]
p2=rut[-2]
p3=rut[-3]
p4=rut[-4]
p5=rut[-5]
p6=rut[-6]
p7=rut[-7]
p8=rut[-8]

d1=int(p1)*2
d2=int(p2)*3
d3=int(p3)*4
d4=int(p4)*5
d5=int(p5)*6
d6=int(p6)*7
d7=int(p7)*2
d8=int(p8)*3


suma=int(d1+d2+d3+d4+d5+d6+d7+d8)
division=suma//11
resto=suma-(11*division)
resta=11-resto

if resta==11:
    dv=str(0)
elif resta==10:
    dv="K"
else:
    dv=str(resta)

print("dv=",dv)