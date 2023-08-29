#codigo verificador
rut=input("numero del Rut:")

if len(rut)==8:
    n1=int(rut[0])
    n2=int(rut[1])
    n3=int(rut[2])
    n4=int(rut[3])
    n5=int(rut[4])
    n6=int(rut[5])
    n7=int(rut[6])
    n8=int(rut[7])

if len(rut)==7:
    n1=0
    n2=int(rut[0])
    n3=int(rut[1])
    n4=int(rut[2])
    n5=int(rut[3])
    n6=int(rut[4])
    n7=int(rut[5])
    n8=int(rut[6])
    

n8=n8*2
n7=n7*3
n6=n6*4
n5=n5*5
n4=n4*6
n3=n3*7
n2=n2*2
n1=n1*3

s=n1+n2+n3+n4+n5+n6+n7+n8

r=s%11
dv=11-r
if dv==10:
    dv="k"
if dv==11:
    dv=0
print("dv=",dv)