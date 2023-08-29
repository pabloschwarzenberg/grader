rut=int(input())
largo=len(str(rut))
suma=0
s=2
for i in range (largo):
    c_n=rut%(10)
    rut=rut//(10)
    p_s=c_n*s
    suma+=p_s
    s+=1
    if s>7:
        s=2
part_e=suma//11
resto=suma-(11*part_e)
sol=11-resto
dv=sol
if dv==11:
    dv=0
elif dv==10:
    dv="k"
print("dv=",dv)
